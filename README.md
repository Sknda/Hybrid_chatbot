# Hybrid Multi-Modal Assistant (HMMA)

A sophisticated Proof-of-Concept (POC) chatbot that integrates traditional rule-based NLP, Generative AI, and Computer Vision into a single conversational interface.

# Project Overview
This project demonstrates a **Hybrid "Triage" Architecture**. It prioritizes precision and cost-efficiency by handling known queries through a local rule-based engine before falling back to the Google Gemini LLM for complex, non-predefined responses. Additionally, it features a vision pipeline for processing image-based data.

# Key Features
- **Hybrid NLP Engine**: Utilizes a tiered response system (JSON-based exact matching ➡️ Generative AI fallback).
- **Computer Vision Suite**: Integrated OpenCV modules for real-time Face Detection and QR Code decoding.
- **Contextual Memory**: Maintains a stateful conversation history using Streamlit Session State.
- **Security-First Design**: Implements environment variable management (`.env`) for sensitive API credentials.
- **Optimized Performance**: Local execution of Vision and Rule-based tasks to minimize latency and API consumption.

# Tech Stack
- **Interface**: Streamlit
- **Language**: Python 3.12
- **AI/LLM**: Google Gemini API
- **Computer Vision**: OpenCV (Open Source Computer Vision Library)
- **Data Handling**: JSON, Python-Dotenv

# Clone the repo
git clone https://github.com/Sknda/Hybrid_chatbot.git

cd Hybrid-Chatbot 

pip install -r requirements.txt

# Run the application
Streamlit run app.py

