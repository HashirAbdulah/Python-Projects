import pyttsx3
import speech_recognition as sp
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import requests

def SpeechtoText():
    recognizer = sp.Recognizer()
    with sp.Microphone() as source:
        print("You got All day,But I Didnt so go Ahead and Say SOMETHING...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input.lower()
        except sp.UnknownValueError:
            print("Unable to UnderStand....Please Speak Again")
            return None

def TexttoSpeech(x):
    engine = pyttsx3.init()            
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    # rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

def open_spotify():
        spotify_path = r"C:\Users\M.Hashir Abdullah\AppData\Roaming\Spotify\Spotify.exe"
        if os.path.exists(spotify_path):
            os.startfile(spotify_path)  # Open the shortcut
        else:
            TexttoSpeech("I couldn't find Spotify at the specified location.")



if __name__ == '__main__':
    extraData = SpeechtoText().lower()
    if "your name" in extraData:
        name = "My name is Semma. How can I help you today?"
        TexttoSpeech(name)
        # TexttoSpeech("I can also play music from your device.")
        # TexttoSpeech("I can also translate your text into English.")
        # TexttoSpeech("I can also send you an email.")
        # TexttoSpeech("I can also tell you about the time zone.")
        # TexttoSpeech("I can also tell you about the sunrise and sunset.")
    elif "can you do" in extraData:
         canDo = f"I am here to help you with anything that i can trained for. What can I do for you? \n I can search for you online, \n I can also tell you a joke. " 
         TexttoSpeech(canDo)
    
    elif 'open browser' in extraData:
        TexttoSpeech(f'Open browser for you.')
        webbrowser.open(f'https://www.google.com/search?q=')

    elif 'open youtube' in extraData:
        TexttoSpeech(f'Opening youtube for you.')
        webbrowser.open("https://www.youtube.com/")

    elif 'google' in extraData:
        TexttoSpeech(f'I have opened google for you.')
        webbrowser.open("https://www.google.com/")

    elif "your age" in extraData:
        age = "I born when you open me"
        TexttoSpeech(age)

    elif "time" in extraData:
        now = datetime.datetime.now()
        date_time = now.strftime("Today is %A, %B %d, %Y. The current time is %I:%M %p.")
        print(date_time)
        TexttoSpeech(date_time)

    elif "search" in extraData:
        TexttoSpeech(f'Tell me what you want to search.')
        search = SpeechtoText()
        webbrowser.open(f'https://www.google.com/search?q={search}')
    
    elif "spotify" in extraData:
        TexttoSpeech(f'Opening Spoteify for you.')
        open_spotify()

    elif "open ai" in extraData:
        TexttoSpeech(f'Opening ChatGPT for you.')
        webbrowser.open("https://chatgpt.com/")

