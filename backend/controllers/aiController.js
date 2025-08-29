// controllers/aiController.js
const { GoogleGenerativeAI } = require('@google/generative-ai');
const fs = require('fs');
const path = require('path');
const geminiService = require('../services/geminiService');
const promptService = require('../services/promptService');

// Main function to plan a trip
const planTrip = async (req, res) => {
  try {
    const { destination, travelers, dates } = req.body;
    
    // Retrieve RAG context
    const ragContext = geminiService.retrieveRAGContext(destination);
    
    // Create prompt using RTFC framework
    const userQuery = `Plan a ${dates[1] - dates[0]}-day trip to ${destination} for ${travelers} travelers`;
    const fullPrompt = promptService.createEnhancedPrompt(userQuery, ragContext);
    
    // Get Gemini model
    const model = geminiService.getGeminiModel();
    
    // Call Gemini API
    const result = await model.generateContent(fullPrompt);
    const response = await result.response;
    const text = response.text();
    
    // Log token usage
    const usage = result.usage;
    console.log(`Prompt tokens: ${usage.promptTokenCount}, Completion tokens: ${usage.candidatesTokenCount}, Total tokens: ${usage.totalTokenCount}`);
    
    // Parse and send the response
    const parsedResponse = JSON.parse(text);
    res.json(parsedResponse);
  } catch (error) {
    console.error('Error planning trip:', error);
    res.status(500).json({ error: 'Failed to plan trip' });
  }
};

module.exports = {
  planTrip
};