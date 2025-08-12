# Smart Travel Assistant

## Overview

The **Smart Travel Assistant** is an AI-powered web app that helps users plan trips by generating personalized itineraries, packing lists, and booking recommendations. It integrates **Generative AI, function calling, structured output, and RAG (Retrieval-Augmented Generation)** to make travel planning easy, fast, and interactive.

---

## Problem Statement

Planning a trip can be time-consuming — travelers often have to browse multiple sites to decide destinations, check travel options, create itineraries, and prepare packing lists. This app centralizes all these tasks into a single AI-driven assistant, reducing manual effort and improving decision-making.

---

## How It Works

1. **User Interaction** – The user enters details like destination, travel dates, number of travelers, and preferences.
2. **Prompting** – The assistant uses carefully designed prompts to generate personalized suggestions.
3. **Function Calling** – AI triggers functions to fetch live data (e.g., flight availability, weather, attraction info).
4. **Structured Output** – The results are returned in JSON format for easy parsing and UI rendering.
5. **RAG Integration** – The AI uses an external knowledge base for travel tips and location-specific details.
6. **Response Rendering** – The app presents a day-by-day itinerary, packing checklist, and booking links in a user-friendly interface.

---

## Features

* **Custom Trip Planning** – AI-generated itineraries based on user preferences.
* **Ticket Booking Integration** – Quick booking links for flights/trains.
* **Personalized Packing List** – Adjusts based on weather and activities.
* **Weather Insights** – Fetches real-time weather forecasts.
* **Multiple Travellers Support** – Plans for groups or individuals.
* **RAG-Powered Travel Tips** – Location-specific advice from stored travel data.

---

## Tech Stack

* **Frontend:** React, Tailwind CSS
* **Backend:** Node.js, Express
* **AI Integration:** OpenAI API (Prompting + Function Calling + Structured Output)
* **RAG Storage:** Vector database (e.g., Pinecone / FAISS) for travel tips
* **APIs:** Flight/Train Booking API, Weather API
* **Deployment:** Vercel / Netlify for frontend, Render for backend

---

## Core AI Concepts in Use

* **Prompt Engineering:** Custom prompts to guide itinerary creation and packing suggestions.
* **Function Calling:** AI calls external APIs to retrieve live travel & weather data.
* **Structured Output:** JSON-formatted AI responses for predictable rendering in UI.
* **RAG (Retrieval-Augmented Generation):** Retrieves relevant travel data from vector DB before generating responses.

---

## Input & Output Examples

**Input Prompt (User):**

```json
{
  "from": "Delhi",
  "destination": "Goa",
  "dates": ["2025-09-15", "2025-09-20"],
  "travellers": 2,
  "preferences": ["beach", "local cuisine", "adventure sports"]
}
```

**AI Output (Structured JSON):**

```json
{
  "itinerary": [
    {
      "day": 1,
      "activities": ["Beach relaxation at Baga", "Local seafood dinner"]
    },
    {
      "day": 2,
      "activities": ["Snorkeling trip", "Visit Anjuna Flea Market"]
    }
  ],
  "packing_list": ["Sunscreen", "Swimwear", "Comfortable sandals", "Sunglasses"],
  "weather_forecast": "Sunny with occasional clouds",
  "booking_links": {
    "flights": "https://example.com/book/flights",
    "hotels": "https://example.com/book/hotels"
  }
}
```

---

## Project Structure

```
smart-travel-assistant/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── routes/
│   ├── services/
│   │   ├── aiService.js
│   │   ├── bookingService.js
│   │   └── weatherService.js
│   ├── app.js
│   └── package.json
│
├── data/
│   └── travel-tips-vector-db/
│
├── README.md
└── .env
```

---

## Future Improvements

* **Voice Assistant Mode** – Plan trips via voice commands.
* **Map Integration** – Visualize itinerary on an interactive map.
* **Chat-Based Trip Modifications** – Refine plans interactively.
* **Photo Suggestions** – AI-recommended Instagram-worthy spots.
* **Multi-language Support** – For global travelers.

---
