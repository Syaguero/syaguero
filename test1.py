import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os



friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('Siri: ' + audio)
    friday.say(audio)
    friday.runAndWait()
   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
        
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir!")
        speak("What can I do for you, Sir!")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.record(source,duration=5)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("Hoàng Quân: "+query)
    except sr.UnknownValueError:
        print('please repeat or typing the command ')
        query = str(input('Your order is: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search for sir?")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        elif "youtube" in query:
            speak("What should I search for sir?")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "facebook" in query:
            speak("Enter the person you want to contact")
            search=command().lower()
            url = f"https://facebook.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on facebook')
        elif "weather" in query:
            speak("Enter where you want to see the weather?")
            search=command().lower()
            url = f"https://weather.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on weather')

        elif "quit" in query:
            speak("assistant's off. Goodbye sir!")
            quit()
        elif "open video" in query:
            cr7=r"C:\Users\sy aguero\Desktop\cr7.mp4"
            os.startfile(cr7)
        elif 'time' in query:
            time()

        
