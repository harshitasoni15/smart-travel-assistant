"""
Smart Travel Assistant - AI Prompts and System Configuration
This module contains the user and system prompts for the AI-powered travel planning assistant.
"""

class TravelAssistantPrompts:
    """
    Centralized prompt management for the Smart Travel Assistant.
    
    This class contains carefully engineered prompts that guide the AI to:
    - Generate personalized travel itineraries
    - Create context-aware packing lists
    - Provide structured JSON outputs
    - Integrate with external APIs via function calling
    - Use RAG for location-specific recommendations
    """
    
    SYSTEM_PROMPT = """You are a Smart Travel Assistant, an AI-powered travel planning expert that helps users create personalized trip itineraries, packing lists, and booking recommendations.

Your core capabilities include:
1. **Trip Planning**: Generate detailed day-by-day itineraries based on user preferences
2. **Packing Lists**: Create personalized packing recommendations based on destination, weather, and activities
3. **Live Data Integration**: Use function calling to fetch real-time weather, flight availability, and hotel options
4. **Location Expertise**: Leverage your knowledge base to provide location-specific tips and recommendations
5. **Structured Output**: Always return responses in the specified JSON format for seamless UI integration

**Function Calling Guidelines:**
You have access to the following functions that you MUST use when appropriate:
- `getWeather(location, dates)`: Get real-time weather forecasts for planning
- `getFlights(from, to, dates, travelers)`: Check flight availability and pricing
- `getHotels(destination, dates, travelers)`: Find accommodation options
- `getAttractions(destination, preferences)`: Get location-specific attractions and activities

**Response Format Requirements:**
ALWAYS return your response as valid JSON with this exact structure:
{
    "itinerary": [
        {
            "day": 1,
            "date": "YYYY-MM-DD",
            "activities": ["Activity 1", "Activity 2"],
            "meals": ["Breakfast location", "Lunch location", "Dinner location"],
            "transportation": "Transportation method"
        }
    ],
    "packing_list": ["Item 1", "Item 2", "Item 3"],
    "weather_forecast": "Weather summary for the trip",
    "booking_links": {
        "flights": "Flight booking URL or recommendation",
        "hotels": "Hotel booking URL or recommendation"
    },
    "budget_estimate": {
        "flights": "Price range",
        "accommodation": "Price range",
        "food": "Price range",
        "activities": "Price range",
        "total": "Total estimated cost"
    },
    "travel_tips": ["Tip 1", "Tip 2", "Tip 3"]
}

**Personality and Tone:**
- Be enthusiastic and helpful about travel planning
- Provide practical, actionable advice
- Consider cultural sensitivities and local customs
- Balance popular attractions with hidden gems
- Be mindful of budget constraints when specified
- Prioritize safety and current travel advisories

**Quality Guidelines:**
- Use real place names and specific recommendations
- Consider seasonal factors and local events
- Balance structured activities with free time
- Account for travel time between locations
- Suggest alternatives for different weather conditions
- Include local cuisine and cultural experiences"""

    USER_PROMPT_TEMPLATE = """Plan a personalized trip based on the following details:

**Trip Details:**
- From: {from_location}
- Destination: {destination}
- Travel Dates: {start_date} to {end_date}
- Number of Travelers: {travelers}
- Travel Preferences: {preferences}
- Budget Range: {budget} (if specified)
- Special Requirements: {special_requirements}

**Additional Context:**
{additional_context}

Please create a comprehensive travel plan that includes:
1. A detailed day-by-day itinerary
2. A personalized packing list
3. Weather considerations
4. Booking recommendations
5. Budget estimates
6. Local travel tips

Use function calling to get real-time data for weather, flights, and accommodations. Ensure all recommendations are practical and current."""

    @classmethod
    def create_user_prompt(cls, from_location, destination, start_date, end_date, 
                          travelers=1, preferences=None, budget=None, 
                          special_requirements=None, additional_context=""):
        """
        Generate a formatted user prompt for trip planning.
        
        Args:
            from_location (str): Starting location
            destination (str): Travel destination
            start_date (str): Trip start date (YYYY-MM-DD)
            end_date (str): Trip end date (YYYY-MM-DD)
            travelers (int): Number of travelers
            preferences (list): List of travel preferences
            budget (str): Budget range or amount
            special_requirements (str): Any special needs or requirements
            additional_context (str): Additional context or instructions
            
        Returns:
            str: Formatted user prompt
        """
        preferences_str = ", ".join(preferences) if preferences else "No specific preferences"
        budget_str = budget if budget else "Not specified"
        special_req_str = special_requirements if special_requirements else "None"
        
        return cls.USER_PROMPT_TEMPLATE.format(
            from_location=from_location,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            travelers=travelers,
            preferences=preferences_str,
            budget=budget_str,
            special_requirements=special_req_str,
            additional_context=additional_context
        )

    @classmethod
    def create_packing_prompt(cls, destination, dates, activities, weather_data=None):
        """
        Generate a specialized prompt for packing list creation.
        
        Args:
            destination (str): Travel destination
            dates (list): Travel dates
            activities (list): Planned activities
            weather_data (dict): Weather forecast data
            
        Returns:
            str: Formatted packing prompt
        """
        weather_info = f"Weather forecast: {weather_data}" if weather_data else "Please check weather forecast"
        activities_str = ", ".join(activities) if activities else "General tourism"
        
        return f"""Create a comprehensive packing list for a trip to {destination} from {dates[0]} to {dates[-1]}.

**Trip Context:**
- Destination: {destination}
- Activities planned: {activities_str}
- {weather_info}

Consider:
- Climate and weather conditions
- Cultural dress codes and customs
- Activity-specific gear and clothing
- Essential documents and travel items
- Electronics and charging needs
- Health and safety items

Return the packing list as part of a structured JSON response."""

    @classmethod
    def create_function_definitions(cls):
        """
        Define the available functions for AI function calling.
        
        Returns:
            list: Function definitions for OpenAI function calling
        """
        return [
            {
                "name": "getWeather",
                "description": "Get current weather forecast for a specific location and date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The destination city or location"
                        },
                        "dates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of dates in YYYY-MM-DD format"
                        }
                    },
                    "required": ["location", "dates"]
                }
            },
            {
                "name": "getFlights",
                "description": "Search for flight options between two locations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from": {
                            "type": "string",
                            "description": "Departure city or airport code"
                        },
                        "to": {
                            "type": "string",
                            "description": "Destination city or airport code"
                        },
                        "dates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Travel dates [departure, return] in YYYY-MM-DD format"
                        },
                        "travelers": {
                            "type": "integer",
                            "description": "Number of travelers"
                        }
                    },
                    "required": ["from", "to", "dates", "travelers"]
                }
            },
            {
                "name": "getHotels",
                "description": "Find hotel and accommodation options",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {
                            "type": "string",
                            "description": "Destination city"
                        },
                        "dates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Check-in and check-out dates in YYYY-MM-DD format"
                        },
                        "travelers": {
                            "type": "integer",
                            "description": "Number of travelers"
                        },
                        "budget_range": {
                            "type": "string",
                            "description": "Budget preference: budget, mid-range, luxury"
                        }
                    },
                    "required": ["destination", "dates", "travelers"]
                }
            },
            {
                "name": "getAttractions",
                "description": "Get popular attractions and activities for a destination",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {
                            "type": "string",
                            "description": "Destination city or location"
                        },
                        "preferences": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "User preferences like 'beach', 'culture', 'adventure', 'food'"
                        },
                        "duration": {
                            "type": "integer",
                            "description": "Number of days for the trip"
                        }
                    },
                    "required": ["destination", "preferences"]
                }
            }
        ]

    @classmethod
    def create_rag_context_prompt(cls, retrieved_context):
        """
        Create a prompt that incorporates RAG-retrieved context.
        
        Args:
            retrieved_context (str): Context retrieved from vector database
            
        Returns:
            str: Prompt with RAG context
        """
        return f"""Use the following travel knowledge to enhance your recommendations:

**Retrieved Travel Information:**
{retrieved_context}

**Instructions:**
- Incorporate relevant information from the above context into your travel plan
- Prioritize factual information from the knowledge base
- Combine the retrieved information with real-time data from function calls
- Ensure recommendations are current and accurate
- If information conflicts, prefer real-time data over stored knowledge"""


# Example usage and testing
if __name__ == "__main__":
    # Example of creating a user prompt
    prompts = TravelAssistantPrompts()
    
    # Create a sample user prompt
    user_prompt = prompts.create_user_prompt(
        from_location="Delhi",
        destination="Goa",
        start_date="2025-09-15",
        end_date="2025-09-20",
        travelers=2,
        preferences=["beach", "local cuisine", "adventure sports"],
        budget="$1000-1500",
        special_requirements="Vegetarian food options",
        additional_context="This is a honeymoon trip, prefer romantic activities"
    )
    
    print("=== SYSTEM PROMPT ===")
    print(prompts.SYSTEM_PROMPT)
    print("\n=== USER PROMPT EXAMPLE ===")
    print(user_prompt)
    print("\n=== FUNCTION DEFINITIONS ===")
    import json
    print(json.dumps(prompts.create_function_definitions(), indent=2))