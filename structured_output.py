"""
Simple Structured Output Implementation for Smart Travel Assistant

This module demonstrates how to implement structured output with the Gemini AI
to ensure consistent, parseable JSON responses for travel planning.
"""

import json
import os
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import google.generativeai as genai
from google.generativeai import GenerationConfig


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class TravelItineraryDay:
    """Structure for a single day's itinerary."""
    day: int
    date: str
    activities: List[str]
    meals: List[str]
    estimated_cost: str
    notes: str = ""


@dataclass
class PackingItem:
    """Structure for packing list items."""
    item: str
    category: str
    essential: bool
    weather_dependent: bool = False


@dataclass
class BookingInfo:
    """Structure for booking information."""
    type: str  # flight, hotel, activity
    name: str
    price: str
    booking_url: str
    details: str


@dataclass
class TravelPlanResponse:
    """Main structured response for travel planning."""
    destination: str
    travel_dates: Dict[str, str]  # start_date, end_date
    total_travelers: int
    itinerary: List[TravelItineraryDay]
    packing_list: List[PackingItem]
    booking_recommendations: List[BookingInfo]
    weather_summary: str
    estimated_total_cost: str
    special_notes: List[str]
    generated_at: str


class StructuredOutputTravelAssistant:
    """
    Simple travel assistant that enforces structured JSON output using Gemini AI.
    
    This implementation focuses on:
    1. Consistent JSON schema validation
    2. Clear data structures using dataclasses
    3. Error handling and fallbacks
    4. Simple usage patterns
    """
    
    def __init__(self, api_key: str = None):
        """Initialize the structured output travel assistant."""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key must be provided or set in GEMINI_API_KEY environment variable")
        
        genai.configure(api_key=self.api_key)
        
        # Configure model for structured output
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=GenerationConfig(
                temperature=0.3,  # Lower temperature for more consistent output
                top_p=0.8,
                top_k=40,
                max_output_tokens=4096,
                response_mime_type="application/json"  # Force JSON output
            )
        )
        
        logger.info("Structured Output Travel Assistant initialized")

    def _create_structured_prompt(self, request_data: Dict[str, Any]) -> str:
        """
        Create a prompt that enforces structured JSON output.
        
        Args:
            request_data: Dictionary with travel request parameters
            
        Returns:
            str: Formatted prompt with JSON schema requirements
        """
        
        # Define the expected JSON schema
        json_schema = {
            "destination": "string - destination city/country",
            "travel_dates": {
                "start_date": "string - YYYY-MM-DD format",
                "end_date": "string - YYYY-MM-DD format"
            },
            "total_travelers": "integer - number of travelers",
            "itinerary": [
                {
                    "day": "integer - day number",
                    "date": "string - YYYY-MM-DD format",
                    "activities": ["string - list of activities"],
                    "meals": ["string - recommended meals/restaurants"],
                    "estimated_cost": "string - cost estimate for the day",
                    "notes": "string - additional notes or tips"
                }
            ],
            "packing_list": [
                {
                    "item": "string - item name",
                    "category": "string - clothing/electronics/toiletries/documents/etc",
                    "essential": "boolean - true if essential",
                    "weather_dependent": "boolean - true if depends on weather"
                }
            ],
            "booking_recommendations": [
                {
                    "type": "string - flight/hotel/activity",
                    "name": "string - name of service/place",
                    "price": "string - price range or estimate",
                    "booking_url": "string - example booking URL",
                    "details": "string - additional details"
                }
            ],
            "weather_summary": "string - weather forecast summary",
            "estimated_total_cost": "string - total trip cost estimate",
            "special_notes": ["string - list of important notes or tips"],
            "generated_at": "string - ISO timestamp"
        }
        
        prompt = f"""
You are a travel planning AI assistant. Create a comprehensive travel plan based on the user's requirements.

User Request:
- From: {request_data.get('from_location', 'Not specified')}
- Destination: {request_data.get('destination', 'Not specified')}
- Start Date: {request_data.get('start_date', 'Not specified')}
- End Date: {request_data.get('end_date', 'Not specified')}
- Travelers: {request_data.get('travelers', 1)}
- Preferences: {', '.join(request_data.get('preferences', []))}
- Budget: {request_data.get('budget', 'Not specified')}
- Special Requirements: {request_data.get('special_requirements', 'None')}

IMPORTANT: You MUST respond with ONLY a valid JSON object that exactly matches this schema:

{json.dumps(json_schema, indent=2)}

Requirements:
1. Generate a realistic day-by-day itinerary for the specified dates
2. Include a practical packing list with proper categorization
3. Provide realistic booking recommendations with example URLs
4. Include weather considerations for the destination and dates
5. Provide cost estimates in the local currency or USD
6. Add helpful tips and special notes
7. Set generated_at to the current ISO timestamp: {datetime.now().isoformat()}
8. Do NOT include any text outside the JSON response
9. Ensure all JSON fields are properly formatted and escape special characters

Respond with only the JSON object:"""