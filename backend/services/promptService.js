// services/promptService.js
const geminiService = require('./geminiService');

// RTFC Framework for prompts
const systemPrompt = {
  role: "Expert travel planning assistant with access to travel knowledge base",
  task: "Generate personalized travel itineraries using provided context",
  format: "Structured JSON responses with clear categorization",
  context: "User preferences, travel constraints, and retrieved knowledge"
};

// Function to create enhanced prompt with RAG
const createEnhancedPrompt = (userQuery, ragContext) => {
  return `
    Based on the following travel knowledge:
    ${JSON.stringify(ragContext, null, 2)}
    
    User Request: ${userQuery}
    
    Generate a comprehensive travel plan with the following details:
    1. Day-by-day itinerary with activities and meals
    2. Recommended packing list based on destination and activities
    3. Weather forecast for the destination during travel dates
    4. Booking recommendations for flights and hotels
    
    Use the following format:
    {
      "itinerary": [
        {
          "day": 1,
          "activities": ["activity1", "activity2"],
          "meals": ["meal1", "meal2"],
          "transportation": "transportation details"
        }
      ],
      "packing_list": ["item1", "item2"],
      "weather_forecast": "weather details",
      "booking_links": {
        "flights": "flight booking link",
        "hotels": "hotel booking link"
      }
    }
  `;
};

// Function to get system prompt
const getSystemPrompt = () => {
  return systemPrompt;
};

module.exports = {
  createEnhancedPrompt,
  getSystemPrompt
};