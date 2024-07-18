import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import subprocess
import os
import requests
from youtubesearchpython import VideosSearch

def get_greeting():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        return "Good morning sir"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon sir"
    else:
        return "Good evening sir"



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def get_weather(city):
    api_key = "9f61445fdb1f89dd29123d90b797c80c"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        weather_report = f"The weather today in {city} is {weather_description}. The temperature is {temperature} degrees Celsius."
    elif data["cod"] == "404":
        weather_report = f"City '{city}' not found. Please check the city name."
    else:
        weather_report = "Sorry, I couldn't retrieve the weather information."

    return weather_report
# # Example usage:
# city = "Hubli"  # Replace with the city you want to get weather information for
# weather_info = get_weather(city)
# print(weather_info)  # Output the weather information

# # Speak the weather information
# speak(weather_info)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "single":
            return f"Here's a joke: {joke['joke']}"
        elif joke["type"] == "twopart":
            return f"Here's a joke: {joke['setup']} ... {joke['delivery']}"
    else:
        return "Sorry, I couldn't fetch a joke at the moment."


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None  # Return None when speech is not recognized
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None  # Return None on request error

def search_in_chrome(query):
    query = query.replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def find_and_play_youtube_video(query):
    query = query.replace("youtube", "").strip()
    videos_search = VideosSearch(query, limit=1)
    results = videos_search.result()
    if results['result']:
        video_url = results['result'][0]['link']
        webbrowser.open(video_url)
    else:
        print("No video results found.")

def open_application(query):
    applications = {
        "notepad": "notepad.exe",
        "vs code": "code",  # Just use 'code' as the command
        "cmd": "cmd.exe",  # Command Prompt
    }
    query = query.replace("open", "").strip().lower()
    if query in applications:
        try:
            if query == "vs code":
                os.system(applications[query])  # Use os.system to execute command
            else:
                subprocess.Popen(applications[query])
        except Exception as e:
            print(f"Error opening {query}: {e}")
    else:
        print("Application not found.")

def main():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Define the welcome and greeting messages
    greeting_message = get_greeting()
    welcome_message = "Hi sir, I'm Alen."
    
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    # Queue the greeting and welcome messages
    engine.say(greeting_message)
    engine.say(welcome_message)
    
    # Block while processing all the currently queued commands
    engine.runAndWait()

    # Initialize the last_joke variable
    last_joke = None

    # Respond to user commands
    while True:
        query = recognize_speech()
        if query is not None:
            if "weather" in query:
                # Extract the city from the query
                city = query.replace("weather in", "").strip()
                weather_report = get_weather(city)
                print(weather_report)   #Output the weather information
                 
                engine.say(weather_report)
                engine.runAndWait()
            elif "search" in query:
                search_in_chrome(query)
                engine.say("Searching in Chrome...")
                engine.runAndWait()
            elif "open" in query:
                open_application(query)
                engine.say("Opening application...")
                engine.runAndWait()
            elif "youtube" in query:
                find_and_play_youtube_video(query)
                engine.say("Playing video on YouTube...")
                engine.runAndWait()
            elif "joke" in query:
                if "another" in query or last_joke is None:
                    last_joke = get_joke()
                original_rate = engine.getProperty('rate')  # Save original rate
                engine.setProperty('rate', 100)  # Adjust speed for joke
                engine.say(last_joke)
                engine.setProperty('rate', original_rate)  # Restore original rate
                engine.runAndWait()
            elif "repeat" in query and last_joke is not None:
                original_rate = engine.getProperty('rate')  # Save original rate
                engine.setProperty('rate', 100)  # Adjust speed for joke
                engine.say(last_joke)
                engine.setProperty('rate', original_rate)  # Restore original rate
                engine.runAndWait()
            elif "exit" in query or "bye" in query:
                engine.say("Goodbye!")
                engine.runAndWait()
                break
            elif "how are you" in query or "how do you do" in query:
                engine.say("I'm fine sir, what about you?")
                engine.runAndWait()
            elif "i am fine " in query or "i am good" in query:
                engine.say("That's good! How can I assist you, sir?")
                engine.runAndWait()
            elif "tell my sister as madam" in query or "call my sister as  madam" in query:
                engine.say("Sure, sir!.  hello madam")
                engine.runAndWait()
            elif "good night" in query:
                engine.say("Good night, sir. Have a good sleep!")
                engine.runAndWait()
            else:
                engine.say("I'm sorry, I didn't understand that.")
                engine.runAndWait()
        else:
            print("No speech recognized. Waiting for the next command...")

if __name__ == "__main__":
    main()
