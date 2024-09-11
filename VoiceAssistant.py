import pyttsx3
import speech_recognition as sp
import webbrowser
import datetime
import pyjokes
import os
import sys

def list_voices():
    """List available voices."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for index, voice in enumerate(voices):
        print(f"Voice {index}: ID={voice.id}, Name={voice.name}, Lang={voice.languages}")

def select_voice():
    """Select a voice from the available options."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} ({voice.id})")

    choice = int(input("Select a voice by number: "))
    if 0 <= choice < len(voices):
        engine.setProperty("voice", voices[choice].id)
        return voices[choice].name
    else:
        print("Invalid choice. Using default voice.")
        return engine.getProperty("voices")[0].name


def SpeechtoText():
    recognizer = sp.Recognizer()
    with sp.Microphone() as source:
        print("You got all day, but I didn't so go ahead and say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input.lower()
        except sp.UnknownValueError:
            print("Unable to understand... Please speak again.")
            return None

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def open_spotify():
    spotify_path = r"C:\Users\M.Hashir Abdullah\AppData\Roaming\Spotify\Spotify.exe"
    if os.path.exists(spotify_path):
        os.startfile(spotify_path)
    else:
        speak("I couldn't find Spotify at the specified location.")

if __name__ == '__main__':
    counter = 0
while True:
    extraData = SpeechtoText()

    if extraData is None:
        counter += 1
        if counter >= 2: 
            speak("I didn't understand twice. Exiting the program.")
            sys.exit()
        else:
            speak("I didn't understand that. Please try again.")
            continue
    else:
        counter = 0 

        if extraData == "hello" or extraData == "hi":
            speak("Hello! How can I help you today?")

        elif "your name" in extraData:
            name = "My name is Semma. How can I help you today?"
            speak(name)
        
        elif "can you do" in extraData:
            canDo = "I am here to help you with anything I am trained for. What can I do for you? \nI can search for you online, \nI can also tell you a joke."
            speak(canDo)
        
        elif "your age" in extraData:
            age = "I was born when you opened me."
            speak(age)

        elif 'open browser' in extraData:
            speak('Opening browser for you.')
            webbrowser.open('https://www.google.com/search?q=')
            break
        
        elif 'open youtube' in extraData:
            speak('Opening YouTube for you.')
            webbrowser.open("https://www.youtube.com/")
            break
        
        elif 'google' in extraData:
            speak('Opening Google for you.')
            webbrowser.open("https://www.google.com/")
            break
        
        elif "time" in extraData:
            now = datetime.datetime.now()
            date_time = now.strftime("Today is %A, %B %d, %Y. The current time is %I:%M %p.")
            print(date_time)
            speak(date_time)
        
        elif "search" in extraData:
            speak('Tell me what you want to search.')
            search = SpeechtoText()
            if search:
                webbrowser.open(f'https://www.google.com/search?q={search}')
                break
        
        elif "spotify" in extraData:
            speak('Opening Spotify for you.')
            open_spotify()
            break
        
        elif "open ai" in extraData:
            speak('Opening ChatGPT for you.')
            webbrowser.open("https://chatgpt.com/")
            break
        
        elif "joke" in extraData:
            joke = pyjokes.get_joke('en', 'neutral')
            print(joke)
            speak(joke)
            break
        else:
            speak("I didn't understand that command. Please try again.")
