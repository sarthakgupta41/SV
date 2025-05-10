import pyttsx3
import datetime   
import speech_recognition as sr
import wikipedia                                  
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good AfterNoon")
    else:
        speak("Good evening")

    speak("Iam your assistant Sir . Please tell me how may I help you ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
 
    except Exception as e:
        #print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to , content):
    pass

def performSearch(query):
    
    """Opens a browser and searches Google."""
    if 'search' in query:
        search_query = query.replace('search', '').strip()
        if search_query:  # If there's something to search for
            speak(f"Searching for {search_query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please tell me what to search.")

def open_website(website_name):
    """Function to open a website based on the user's command."""
    speak(f"Opening {website_name}")
    webbrowser.open(f"http://{website_name}.com")



if __name__ == "__main__":
    speak('Hello sir Project created by - Sarthak.V')
    wishMe()
    while (True):
        query = takeCommand().lower()
       
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'how are you' in query:
            speak("Iam Fine Sir")
        elif 'who is sarthak' in query:
            speak("Sarthak is a new generation coder . He also has code this program  , Currently learning Python")
        elif 'is my sister dumb' in query:
            speak("Yes Siddhi Didi is Stupid")
        elif ' who are you' in query:
            speak("Iam a Jarvis AI Robot , iam very intelleigent , you can ask me anything7 created by Sarthak.V")
        elif 'search' in query:
            performSearch(query)
        elif 'open' in query:
            website_name = query.split('open')[-1].strip()
            open_website(website_name)
        elif 'who is Daksh'in query:
            speak('He is Sarthak s freind and a very good all rounder also known is Kholi ') 
        
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        
        # elif 'open code':
        #     os.system("C:\Users\hp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
