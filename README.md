# Alen - Voice Assistant
Overview
This project is a personal voice assistant named Alen that can respond to voice commands, provide weather updates, tell jokes, search the web, open applications, and play YouTube videos. The assistant uses text-to-speech (TTS) to interact with the user and supports various commands for seamless interaction.

Features
Voice Commands: Recognizes voice commands using the SpeechRecognition library.
Weather Updates: Fetches current weather information for any city.
Jokes: Provides jokes on demand.
Web Search: Searches the web using Google Chrome.
YouTube Search: Plays videos based on YouTube search queries.
Application Launch: Opens common applications like Notepad, VS Code, and Command Prompt.
Friendly Greetings: Offers personalized greetings and responses based on the time of day.

Technologies Used
Python: Core language for the project.
Pyttsx3: For text-to-speech conversion.
SpeechRecognition: For capturing and processing voice input.
OpenWeatherMap API: For fetching real-time weather updates.
YouTubeSearchPython: For searching and playing YouTube videos.
Subprocess & OS: For launching applications.
Installation
Prerequisites
Install the required Python libraries:

bash
Copy code
pip install pyttsx3 SpeechRecognition requests youtubesearchpython
Optionally, you can install the OpenWeatherMap API for weather updates. Sign up at OpenWeather and get your API key.

Running the Project
Clone the repository and navigate to the project directory.

Run the Python script:

bash
Copy code
python voice_assistant.py
The assistant will greet you and start listening for voice commands.

Supported Commands
Weather: Ask for the weather by saying, "What's the weather in [city]?".
Search the Web: Say, "Search [your query]" to perform a Google search.
YouTube: To play a YouTube video, say, "Play [video name] on YouTube".
Jokes: Ask for a joke by saying, "Tell me a joke". You can also ask for another joke or repeat the last one.
Open Applications: Commands like "Open Notepad", "Open VS Code", or "Open Command Prompt" will open these applications.
Greetings: You can say "How are you?" or "Good morning/afternoon/evening" for friendly interactions.
Goodbye: End the conversation by saying "Goodbye" or "Exit".

Example Usage
# Example of commands you can give to Alen:
"What's the weather in New York?"
"Play Despacito on YouTube"
"Open Notepad"
"Tell me a joke"
Configuration
Weather API
To enable weather reports, get an API key from OpenWeather and replace the placeholder key in the get_weather function:
python

Contribution
Feel free to open issues, submit pull requests, or suggest improvements.
