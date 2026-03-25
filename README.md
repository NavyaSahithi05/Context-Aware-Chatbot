# Context-Aware Conversational Chatbot

## Description
This project is a context-aware chatbot developed for a customer support use case. It maintains conversation context across multiple turns and provides coherent responses.

## Features
- Intent Recognition (rule-based NLP)
- Context Memory (tracks previous interactions)
- Multi-turn conversation handling
- Web-based interface using Flask

## Tech Stack
- Python
- Flask
- HTML, CSS, JavaScript

## Architecture
User Input → Intent Detection → Context Manager → Response Generator → Bot Reply

## Context Management
The chatbot stores:
- Last user intent
- Order ID (if provided)

This enables the bot to understand follow-up inputs and maintain conversation flow.

## Sample Conversation

User: Hi  
Bot: Hello! How can I assist you?

User: Where is my order?  
Bot: Please provide your order ID.

User: 12345  
Bot: Your order 12345 is out for delivery.

## How to Run

1. Install Flask: pip install flask
2. Run the app: python app.py
3. Open browser: http://127.0.0.1:5000/

## Future Improvements
- Use ML models for intent recognition
- Add database for storing user sessions
- Improve UI/UX
