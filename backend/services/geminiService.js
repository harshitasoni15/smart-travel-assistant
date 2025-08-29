// services/geminiService.js
const { GoogleGenerativeAI } = require('@google/generative-ai');
const fs = require('fs');
const path = require('path');

// Initialize Gemini
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

// Load travel knowledge
const travelKnowledgePath = path.join(__dirname, '../data/travelKnowledge.json');
const travelKnowledge = JSON.parse(fs.readFileSync(travelKnowledgePath, 'utf8'));

// Function to get Gemini model with specific configuration
const getGeminiModel = (config = {}) => {
  const geminiConfig = require('../config/geminiConfig');
  
  // Merge config with default config
  const modelConfig = {
    ...geminiConfig,
    ...config,
    safetySettings: config.safetySettings || geminiConfig.safetySettings,
    generationConfig: {
      ...geminiConfig.generationConfig,
      ...config.generationConfig
    }
  };
  
  return genAI.getGenerativeModel(modelConfig);
};

// Function to retrieve RAG context
const retrieveRAGContext = (destination) => {
  // For now, just return the knowledge for the destination
  // In future iterations, this will include more sophisticated retrieval
  return {
    destination: travelKnowledge.destinations[destination.toLowerCase()] || {},
    general: travelKnowledge.general
  };
};

module.exports = {
  getGeminiModel,
  retrieveRAGContext
};