**Metro Chatbot – AI Travel Assistant
Project Overview**

The Metro Chatbot is an intelligent travel assistant designed to help users get quick information about metro services. The chatbot can answer queries related to metro routes, fare details, timings, and station information using a Natural Language Processing (NLP) based backend.

This project simulates a real-world metro information system where users can interact through a chat interface and receive instant responses.

**Features**

Chat-based interface for user interaction
Natural Language Processing for understanding user queries
Provides metro route information
Fare calculation between stations
Metro timing information
Station details and travel guidance
Fast response using a Flask backend

**Technologies Used**

Technology	Purpose
Python	Backend programming
Flask	Web framework
HTML	Frontend structure
CSS	UI styling
JavaScript	Frontend interaction
JSON	Metro data storage
NLP Logic	Query processing

**Project Structure**
metro_chatbot
│
├── app.py
├── requirements.txt
│
├── chatbot
│   ├── metro_logic.py
│   ├── nlp_engine.py
│   └── __init__.py
│
├── data
│   └── metro_data.json
│
├── templates
│   └── index.html
│
└── static

 **Installation & Setup**

**Clone the Repository**
git clone https://github.com/AffraAbdulRahman/Metro_Chatbot.git
cd Metro-Chatbot

**Create Virtual Environment**
python -m venv venv

**Activate Environment**
Windows
  venv\Scripts\activate
Mac/Linux
  source venv/bin/activate
  
**Install Dependencies**
pip install -r requirements.txt

**Run the Application**
python app.py

**Open in Browser**
http://127.0.0.1:5000

**How It Works**
User enters a query in the chatbot interface.
The query is processed using the NLP engine.
The system matches the intent with metro data.
The chatbot returns the correct response such as route, fare, or timing.

**Example Queries**

"What is the fare from Airport to Central?"
"Show metro timings"
"How to go from Anna Nagar to Guindy?"
"List metro stations"
