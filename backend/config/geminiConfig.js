// config/geminiConfig.js
const geminiConfig = {
  model: "gemini-2.0-flash",
  safetySettings: [
    {
      category: "HARM_CATEGORY_HARASSMENT",
      threshold: "BLOCK_MEDIUM_AND_ABOVE"
    }
  ],
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: {}
  }
};

module.exports = geminiConfig;