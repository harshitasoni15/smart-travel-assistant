"""
Dynamic Prompting Example

Dynamic prompting adapts the prompt based on user input, context, or previous 
responses. It can modify the prompt structure, add relevant examples, or 
adjust the complexity based on the situation.
"""

def dynamic_prompting_example():
    """
    Example of dynamic prompting that adapts based on user preferences
    """
    
    # Simulated user preferences
    user_preferences = {
        "budget": "mid-range",
        "travel_style": "cultural",
        "group_size": 2,
        "interests": ["museums", "local_food", "history"]
    }
    
    # Dynamic prompt construction based on user input
    base_prompt = "Plan a travel itinerary that matches the following preferences:\n\n"
    
    # Add budget-specific guidance
    budget_guidance = {
        "budget": f"Budget Level: {user_preferences['budget']} - Include moderately priced accommodations and dining options.\n",
        "luxury": "Budget Level: luxury - Include high-end hotels, fine dining, and premium experiences.\n",
        "backpacker": "Budget Level: budget - Focus on hostels, street food, and free/low-cost activities.\n"
    }
    
    # Add travel style specific instructions
    style_guidance = {
        "cultural": "Travel Style: Cultural - Emphasize museums, historical sites, and local traditions.\n",
        "adventure": "Travel Style: Adventure - Focus on outdoor activities, hiking, and thrilling experiences.\n",
        "relaxation": "Travel Style: Relaxation - Prioritize spas, beaches, and leisurely activities.\n"
    }
    
    # Build dynamic prompt
    dynamic_prompt = base_prompt
    dynamic_prompt += budget_guidance.get(user_preferences["budget"], "")
    dynamic_prompt += style_guidance.get(user_preferences["travel_style"], "")
    dynamic_prompt += f"Group Size: {user_preferences['group_size']} people\n"
    dynamic_prompt += f"Special Interests: {', '.join(user_preferences['interests'])}\n\n"
    dynamic_prompt += "Destination: Prague, Czech Republic\nDuration: 4 days\n\n"
    dynamic_prompt += "Please provide a detailed itinerary that matches these preferences."
    
    print("Dynamic Prompt Example:")
    print("User Preferences:", user_preferences)
    print("\nGenerated Dynamic Prompt:")
    print(dynamic_prompt)
    print("\n" + "="*50 + "\n")
    
    return dynamic_prompt

def adaptive_recommendation_system():
    """
    Dynamic prompting system that adapts based on previous responses
    """
    
    # Simulated conversation history
    conversation_context = {
        "previous_destinations": ["Paris", "Rome"],
        "liked_activities": ["art museums", "food tours"],
        "disliked_activities": ["crowded beaches", "shopping"],
        "season_preference": "spring"
    }
    
    # Build contextual prompt
    contextual_prompt = "Based on your travel history and preferences:\n\n"
    
    if conversation_context["previous_destinations"]:
        contextual_prompt += f"You've enjoyed visiting: {', '.join(conversation_context['previous_destinations'])}\n"
    
    if conversation_context["liked_activities"]:
        contextual_prompt += f"You particularly enjoyed: {', '.join(conversation_context['liked_activities'])}\n"
    
    if conversation_context["disliked_activities"]:
        contextual_prompt += f"You want to avoid: {', '.join(conversation_context['disliked_activities'])}\n"
    
    contextual_prompt += f"Preferred travel season: {conversation_context['season_preference']}\n\n"
    contextual_prompt += "Recommend your next destination and explain why it matches your preferences."
    
    print("Adaptive Recommendation System:")
    print("Context:", conversation_context)
    print("\nGenerated Contextual Prompt:")
    print(contextual_prompt)
    
    return contextual_prompt

def weather_based_dynamic_prompt():
    """
    Dynamic prompting that adapts based on current weather conditions
    """
    
    # Simulated weather data
    weather_conditions = {
        "destination": "London",
        "current_weather": "rainy",
        "temperature": "15°C",
        "forecast": "rain for next 3 days"
    }
    
    # Adapt prompt based on weather
    weather_prompt = f"Current weather in {weather_conditions['destination']}:\n"
    weather_prompt += f"Condition: {weather_conditions['current_weather']}\n"
    weather_prompt += f"Temperature: {weather_conditions['temperature']}\n"
    weather_prompt += f"Forecast: {weather_conditions['forecast']}\n\n"
    
    # Add weather-specific recommendations
    if weather_conditions["current_weather"] == "rainy":
        weather_prompt += "Given the rainy weather, recommend indoor activities, museums, covered markets, and cozy cafes. "
        weather_prompt += "Also suggest what to pack and how to make the most of a rainy day in the city."
    elif weather_conditions["current_weather"] == "sunny":
        weather_prompt += "With sunny weather, focus on outdoor activities, parks, walking tours, and outdoor dining options."
    
    print("Weather-Based Dynamic Prompt:")
    print("Weather Data:", weather_conditions)
    print("\nGenerated Weather-Adaptive Prompt:")
    print(weather_prompt)
    
    return weather_prompt

if __name__ == "__main__":
    dynamic_prompting_example()
    print()
    adaptive_recommendation_system()
    print()
    weather_based_dynamic_prompt()