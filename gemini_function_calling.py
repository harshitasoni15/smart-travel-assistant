"""
Smart Travel Assistant - Gemini API Function Calling Implementation
This module provides the Gemini API integration with function calling capabilities
for the Smart Travel Assistant application.
"""

import json
import os
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, date
import google.generativeai as genai
from google.generativeai import GenerationConfig
from google.generativeai.types import FunctionDeclaration, Tool
import requests
from prompts import TravelAssistantPrompts

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GeminiTravelAssistant:
    """
    Gemini API integration for the Smart Travel Assistant.
    
    This class handles:
    - Gemini API configuration and authentication
    - Function calling for external services (weather, flights, hotels, attractions)
    - Structured output generation for travel planning
    - RAG integration for enhanced recommendations
    """
    
    def __init__(self, api_key: str = None, weather_api_key: str = None):
        """
        Initialize the Gemini Travel Assistant.
        
        Args:
            api_key (str): Gemini API key. If None, will try to read from GEMINI_API_KEY env var
            weather_api_key (str): Weather API key for real-time weather data
        """
        # Configure Gemini API
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key must be provided or set in GEMINI_API_KEY environment variable")
        
        genai.configure(api_key=self.api_key)
        
        # Initialize the model with function calling capabilities
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            tools=[self._create_function_tools()],
            generation_config=GenerationConfig(
                temperature=0.7,
                top_p=0.8,
                top_k=40,
                max_output_tokens=4096,
                response_mime_type="application/json"
            )
        )
        
        # External API keys
        self.weather_api_key = weather_api_key or os.getenv('WEATHER_API_KEY')
        
        # Initialize prompts
        self.prompts = TravelAssistantPrompts()
        
        logger.info("Gemini Travel Assistant initialized successfully")

    def _create_function_tools(self) -> Tool:
        """
        Create function declarations for Gemini function calling.
        
        Returns:
            Tool: Gemini Tool object with function declarations
        """
        # Weather function
        get_weather = FunctionDeclaration(
            name="getWeather",
            description="Get real-time weather forecast for a specific location and date range",
            parameters={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The destination city or location (e.g., 'Goa', 'New Delhi', 'Mumbai')"
                    },
                    "dates": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Array of dates in YYYY-MM-DD format for the forecast period"
                    }
                },
                "required": ["location", "dates"]
            }
        )
        
        # Flight search function
        get_flights = FunctionDeclaration(
            name="getFlights",
            description="Search for flight options between two locations with pricing and availability",
            parameters={
                "type": "object",
                "properties": {
                    "from_location": {
                        "type": "string",
                        "description": "Departure city or airport code (e.g., 'Delhi', 'DEL', 'Mumbai')"
                    },
                    "to_location": {
                        "type": "string",
                        "description": "Destination city or airport code (e.g., 'Goa', 'GOI', 'Bangalore')"
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in YYYY-MM-DD format"
                    },
                    "return_date": {
                        "type": "string",
                        "description": "Return date in YYYY-MM-DD format (optional for one-way trips)"
                    },
                    "travelers": {
                        "type": "integer",
                        "description": "Number of travelers (adults)"
                    }
                },
                "required": ["from_location", "to_location", "departure_date", "travelers"]
            }
        )
        
        # Hotel search function
        get_hotels = FunctionDeclaration(
            name="getHotels",
            description="Find hotel and accommodation options with pricing and availability",
            parameters={
                "type": "object",
                "properties": {
                    "destination": {
                        "type": "string",
                        "description": "Destination city or location for accommodation search"
                    },
                    "check_in": {
                        "type": "string",
                        "description": "Check-in date in YYYY-MM-DD format"
                    },
                    "check_out": {
                        "type": "string",
                        "description": "Check-out date in YYYY-MM-DD format"
                    },
                    "travelers": {
                        "type": "integer",
                        "description": "Number of travelers requiring accommodation"
                    },
                    "budget_category": {
                        "type": "string",
                        "enum": ["budget", "mid-range", "luxury"],
                        "description": "Budget preference category for accommodation"
                    }
                },
                "required": ["destination", "check_in", "check_out", "travelers"]
            }
        )
        
        # Attractions function
        get_attractions = FunctionDeclaration(
            name="getAttractions",
            description="Get popular attractions, activities, and points of interest for a destination",
            parameters={
                "type": "object",
                "properties": {
                    "destination": {
                        "type": "string",
                        "description": "Destination city or location to search attractions for"
                    },
                    "preferences": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "User preferences like 'beach', 'culture', 'adventure', 'food', 'nightlife', 'shopping'"
                    },
                    "trip_duration": {
                        "type": "integer",
                        "description": "Number of days for the trip to tailor recommendations"
                    }
                },
                "required": ["destination", "preferences"]
            }
        )
        
        return Tool(function_declarations=[get_weather, get_flights, get_hotels, get_attractions])

    def getWeather(self, location: str, dates: List[str]) -> Dict[str, Any]:
        """
        Fetch real-time weather data for the specified location and dates.
        
        Args:
            location (str): Location name
            dates (List[str]): List of dates in YYYY-MM-DD format
            
        Returns:
            Dict: Weather forecast data
        """
        try:
            if not self.weather_api_key:
                # Return mock weather data if no API key is available
                return {
                    "location": location,
                    "forecast": [
                        {
                            "date": date_str,
                            "temperature_high": 28,
                            "temperature_low": 22,
                            "condition": "Partly cloudy",
                            "humidity": 65,
                            "wind_speed": 12,
                            "precipitation_chance": 20
                        } for date_str in dates
                    ],
                    "summary": f"Pleasant weather expected in {location} with temperatures ranging from 22°C to 28°C"
                }
            
            # For demonstration, using OpenWeatherMap API format
            # In production, replace with your preferred weather API
            weather_data = {
                "location": location,
                "forecast": [],
                "summary": ""
            }
            
            for date_str in dates:
                # Mock API call - replace with actual weather API integration
                forecast_day = {
                    "date": date_str,
                    "temperature_high": 30,
                    "temperature_low": 24,
                    "condition": "Sunny",
                    "humidity": 60,
                    "wind_speed": 8,
                    "precipitation_chance": 10
                }
                weather_data["forecast"].append(forecast_day)
            
            weather_data["summary"] = f"Generally sunny weather in {location} with highs around 30°C"
            
            logger.info(f"Weather data fetched for {location}")
            return weather_data
            
        except Exception as e:
            logger.error(f"Error fetching weather data: {e}")
            return {
                "location": location,
                "error": "Unable to fetch weather data",
                "summary": "Weather information unavailable"
            }

    def getFlights(self, from_location: str, to_location: str, departure_date: str, 
                   return_date: str = None, travelers: int = 1) -> Dict[str, Any]:
        """
        Search for flight options between locations.
        
        Args:
            from_location (str): Departure location
            to_location (str): Destination location
            departure_date (str): Departure date
            return_date (str): Return date (optional)
            travelers (int): Number of travelers
            
        Returns:
            Dict: Flight search results
        """
        try:
            # Mock flight data - replace with actual flight API integration
            flight_data = {
                "search_criteria": {
                    "from": from_location,
                    "to": to_location,
                    "departure": departure_date,
                    "return": return_date,
                    "travelers": travelers
                },
                "outbound_flights": [
                    {
                        "airline": "IndiGo",
                        "flight_number": "6E 123",
                        "departure_time": "08:30",
                        "arrival_time": "10:45",
                        "duration": "2h 15m",
                        "price": f"₹{4500 * travelers}",
                        "booking_url": "https://www.goindigo.in/booking"
                    },
                    {
                        "airline": "Air India",
                        "flight_number": "AI 456",
                        "departure_time": "14:20",
                        "arrival_time": "16:40",
                        "duration": "2h 20m",
                        "price": f"₹{5200 * travelers}",
                        "booking_url": "https://www.airindia.in/booking"
                    }
                ],
                "return_flights": [] if not return_date else [
                    {
                        "airline": "IndiGo",
                        "flight_number": "6E 789",
                        "departure_time": "18:15",
                        "arrival_time": "20:30",
                        "duration": "2h 15m",
                        "price": f"₹{4800 * travelers}",
                        "booking_url": "https://www.goindigo.in/booking"
                    }
                ],
                "summary": f"Found multiple flight options from {from_location} to {to_location}"
            }
            
            logger.info(f"Flight data fetched for {from_location} to {to_location}")
            return flight_data
            
        except Exception as e:
            logger.error(f"Error fetching flight data: {e}")
            return {
                "error": "Unable to fetch flight data",
                "summary": "Flight information unavailable"
            }

    def getHotels(self, destination: str, check_in: str, check_out: str, 
                  travelers: int = 1, budget_category: str = "mid-range") -> Dict[str, Any]:
        """
        Search for hotel accommodations.
        
        Args:
            destination (str): Destination city
            check_in (str): Check-in date
            check_out (str): Check-out date
            travelers (int): Number of travelers
            budget_category (str): Budget preference
            
        Returns:
            Dict: Hotel search results
        """
        try:
            # Mock hotel data - replace with actual hotel API integration
            price_ranges = {
                "budget": (1500, 3000),
                "mid-range": (3000, 8000),
                "luxury": (8000, 25000)
            }
            
            base_price = price_ranges.get(budget_category, price_ranges["mid-range"])[0]
            
            hotel_data = {
                "search_criteria": {
                    "destination": destination,
                    "check_in": check_in,
                    "check_out": check_out,
                    "travelers": travelers,
                    "budget_category": budget_category
                },
                "hotels": [
                    {
                        "name": f"Hotel Paradise {destination}",
                        "category": budget_category,
                        "rating": 4.2,
                        "price_per_night": f"₹{base_price}",
                        "amenities": ["Free WiFi", "Swimming Pool", "Restaurant", "Room Service"],
                        "location": f"Central {destination}",
                        "booking_url": "https://www.booking.com"
                    },
                    {
                        "name": f"Grand {destination} Resort",
                        "category": budget_category,
                        "rating": 4.5,
                        "price_per_night": f"₹{int(base_price * 1.3)}",
                        "amenities": ["Spa", "Beach Access", "Multiple Restaurants", "Gym"],
                        "location": f"Beach Area, {destination}",
                        "booking_url": "https://www.agoda.com"
                    }
                ],
                "summary": f"Found {budget_category} hotels in {destination} starting from ₹{base_price} per night"
            }
            
            logger.info(f"Hotel data fetched for {destination}")
            return hotel_data
            
        except Exception as e:
            logger.error(f"Error fetching hotel data: {e}")
            return {
                "error": "Unable to fetch hotel data",
                "summary": "Hotel information unavailable"
            }

    def getAttractions(self, destination: str, preferences: List[str], 
                      trip_duration: int = 3) -> Dict[str, Any]:
        """
        Get attractions and activities for a destination.
        
        Args:
            destination (str): Destination city
            preferences (List[str]): User preferences
            trip_duration (int): Trip duration in days
            
        Returns:
            Dict: Attractions and activities data
        """
        try:
            # Mock attractions data - replace with actual attractions API
            attraction_categories = {
                "beach": ["Baga Beach", "Calangute Beach", "Anjuna Beach"],
                "culture": ["Old Goa Churches", "Goa State Museum", "Fontainhas Latin Quarter"],
                "adventure": ["Water Sports at Baga", "Scuba Diving", "Parasailing"],
                "food": ["Thalassa Restaurant", "Fisherman's Wharf", "Local Fish Markets"],
                "nightlife": ["Club Cubana", "Tito's", "Casino Palms"],
                "shopping": ["Anjuna Flea Market", "Mapusa Market", "Panaji Shopping"]
            }
            
            recommended_attractions = []
            for pref in preferences:
                if pref.lower() in attraction_categories:
                    recommended_attractions.extend(attraction_categories[pref.lower()][:2])
            
            # Add some general attractions
            recommended_attractions.extend(["Fort Aguada", "Dudhsagar Falls"])
            
            attractions_data = {
                "destination": destination,
                "preferences": preferences,
                "recommended_attractions": recommended_attractions[:trip_duration * 2],
                "day_wise_suggestions": {
                    f"day_{i+1}": recommended_attractions[i*2:(i+1)*2] 
                    for i in range(min(trip_duration, len(recommended_attractions)//2))
                },
                "summary": f"Found {len(recommended_attractions)} attractions matching your preferences in {destination}"
            }
            
            logger.info(f"Attractions data fetched for {destination}")
            return attractions_data
            
        except Exception as e:
            logger.error(f"Error fetching attractions data: {e}")
            return {
                "error": "Unable to fetch attractions data",
                "summary": "Attractions information unavailable"
            }

    def _execute_function_call(self, function_call) -> Dict[str, Any]:
        """
        Execute the appropriate function based on the function call from Gemini.
        
        Args:
            function_call: Function call object from Gemini
            
        Returns:
            Dict: Function execution result
        """
        function_name = function_call.name
        function_args = dict(function_call.args)
        
        logger.info(f"Executing function: {function_name} with args: {function_args}")
        
        try:
            if function_name == "getWeather":
                return self.getWeather(
                    location=function_args["location"],
                    dates=function_args["dates"]
                )
            elif function_name == "getFlights":
                return self.getFlights(
                    from_location=function_args["from_location"],
                    to_location=function_args["to_location"],
                    departure_date=function_args["departure_date"],
                    return_date=function_args.get("return_date"),
                    travelers=function_args["travelers"]
                )
            elif function_name == "getHotels":
                return self.getHotels(
                    destination=function_args["destination"],
                    check_in=function_args["check_in"],
                    check_out=function_args["check_out"],
                    travelers=function_args["travelers"],
                    budget_category=function_args.get("budget_category", "mid-range")
                )
            elif function_name == "getAttractions":
                return self.getAttractions(
                    destination=function_args["destination"],
                    preferences=function_args["preferences"],
                    trip_duration=function_args.get("trip_duration", 3)
                )
            else:
                return {"error": f"Unknown function: {function_name}"}
                
        except Exception as e:
            logger.error(f"Error executing function {function_name}: {e}")
            return {"error": f"Function execution failed: {str(e)}"}

    def plan_trip(self, from_location: str, destination: str, start_date: str, 
                  end_date: str, travelers: int = 1, preferences: List[str] = None,
                  budget: str = None, special_requirements: str = None,
                  rag_context: str = None) -> Tuple[Dict[str, Any], str]:
        """
        Generate a comprehensive travel plan using Gemini AI with function calling.
        
        Args:
            from_location (str): Starting location
            destination (str): Travel destination
            start_date (str): Trip start date (YYYY-MM-DD)
            end_date (str): Trip end date (YYYY-MM-DD)
            travelers (int): Number of travelers
            preferences (List[str]): Travel preferences
            budget (str): Budget range
            special_requirements (str): Special requirements
            rag_context (str): Additional context from RAG system
            
        Returns:
            Tuple[Dict[str, Any], str]: (Parsed response, Raw response)
        """
        try:
            # Create the user prompt
            user_prompt = self.prompts.create_user_prompt(
                from_location=from_location,
                destination=destination,
                start_date=start_date,
                end_date=end_date,
                travelers=travelers,
                preferences=preferences or [],
                budget=budget,
                special_requirements=special_requirements,
                additional_context=rag_context or ""
            )
            
            # Prepare messages
            messages = [
                {"role": "system", "parts": [self.prompts.SYSTEM_PROMPT]},
                {"role": "user", "parts": [user_prompt]}
            ]
            
            logger.info(f"Starting trip planning for {destination}")
            
            # Start conversation with Gemini
            chat = self.model.start_chat()
            response = chat.send_message(user_prompt)
            
            # Handle function calls if any
            while response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                function_result = self._execute_function_call(function_call)
                
                # Send function result back to model
                response = chat.send_message(
                    genai.types.content.Content(
                        parts=[genai.types.content.Part(
                            function_response=genai.types.content.FunctionResponse(
                                name=function_call.name,
                                response=function_result
                            )
                        )]
                    )
                )
            
            # Extract the final response text
            raw_response = response.text
            
            # Parse JSON response
            try:
                parsed_response = json.loads(raw_response)
            except json.JSONDecodeError:
                # If JSON parsing fails, create a structured response
                parsed_response = {
                    "error": "Failed to parse AI response",
                    "raw_response": raw_response
                }
            
            logger.info(f"Trip planning completed for {destination}")
            return parsed_response, raw_response
            
        except Exception as e:
            logger.error(f"Error in trip planning: {e}")
            error_response = {
                "error": f"Trip planning failed: {str(e)}",
                "destination": destination,
                "status": "error"
            }
            return error_response, str(e)

    def get_packing_list(self, destination: str, dates: List[str], 
                        activities: List[str], weather_data: Dict = None) -> Dict[str, Any]:
        """
        Generate a personalized packing list for the trip.
        
        Args:
            destination (str): Travel destination
            dates (List[str]): Travel dates
            activities (List[str]): Planned activities
            weather_data (Dict): Weather forecast data
            
        Returns:
            Dict: Packing list recommendations
        """
        try:
            # Create packing prompt
            packing_prompt = self.prompts.create_packing_prompt(
                destination=destination,
                dates=dates,
                activities=activities,
                weather_data=weather_data
            )
            
            # Generate packing list using Gemini
            response = self.model.generate_content(packing_prompt)
            
            try:
                packing_response = json.loads(response.text)
            except json.JSONDecodeError:
                # Fallback packing list
                packing_response = {
                    "packing_list": [
                        "Comfortable walking shoes",
                        "Sunscreen and sunglasses",
                        "Weather-appropriate clothing",
                        "Travel documents and ID",
                        "Phone charger and power bank",
                        "First aid kit",
                        "Camera or smartphone",
                        "Travel adapter (if needed)"
                    ],
                    "destination": destination,
                    "weather_considerations": "Pack according to local weather conditions"
                }
            
            return packing_response
            
        except Exception as e:
            logger.error(f"Error generating packing list: {e}")
            return {
                "error": f"Failed to generate packing list: {str(e)}",
                "destination": destination
            }


# Example usage and testing functions
def example_usage():
    """Example of how to use the GeminiTravelAssistant class."""
    
    # Initialize the assistant (you'll need to set your API keys)
    assistant = GeminiTravelAssistant()
    
    # Plan a trip
    result, raw = assistant.plan_trip(
        from_location="Delhi",
        destination="Goa",
        start_date="2025-09-15",
        end_date="2025-09-20",
        travelers=2,
        preferences=["beach", "local cuisine", "adventure sports"],
        budget="$1000-1500",
        special_requirements="Vegetarian food options"
    )
    
    print("=== TRIP PLANNING RESULT ===")
    print(json.dumps(result, indent=2))
    
    # Generate packing list
    packing_list = assistant.get_packing_list(
        destination="Goa",
        dates=["2025-09-15", "2025-09-20"],
        activities=["beach", "water sports", "sightseeing"]
    )
    
    print("\n=== PACKING LIST ===")
    print(json.dumps(packing_list, indent=2))


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Run example (commented out to avoid API calls without keys)
    # example_usage()
    
    print("Gemini Travel Assistant module loaded successfully!")
    print("Set GEMINI_API_KEY environment variable to use the assistant.")