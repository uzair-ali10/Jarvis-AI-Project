import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
#sapii5 is an speech to text coverter tool from microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    speak("connecting to database")
    speak("initializeing jarvis")
    speak("establishing a secure connection")
    speak("connection established")
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning,Sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon,Sir!")
    else:
        speak("Good evening,Sir!")
    speak("Jarvis here,how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia,this may take a minute...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            """speak("do you want to know more")
            query = takeCommand().lower()
            if "yes" in query:
                query = query.replace("wikipedia",query)
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                print(results)
                speak(results)"""

        if 'stop jarvis' in query:
            speak("thanks for your time!,have a nice day!")
            exit()
            
        if 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')
            
        if 'thanks' in query or 'thank you' in query:
            speak('My pleasure, sir')
        
        if "open google" in query:
            webbrowser.open('google.com')
        if "what time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,currently the time is {strTime}")
        if "open pycharm" in query:
            codePath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"  ##<---- THIS PATH IS SET FOR MY COMPUTER, IT MAY DIFFER WITH YOUR'S
            speak(f"Alright sir,opening {query}")
            os.startfile(codePath)
            speak(f"Done!")
        if "open youtube" in query:
            webbrowser.open('youtube.com')
        if "open gmail" in query:
            webbrowser.open('gmail.com')
         if "open github" in query:
            webbrowser.open(guthub.com)
            

  
