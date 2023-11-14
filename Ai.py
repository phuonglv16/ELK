import pyttsx3 
import datetime
import pyaudio
import speech_recognition as sr
import webbrowser as wb
import os

DQ=pyttsx3.init()
voice=DQ.getProperty('voices')#để nói dc  giọng nói 
DQ.setProperty('voice',voice[1].id)#chọn giọng nữ(0) là giọng nam 

def speak(audio):
    print('Phuong:'+ audio)
    DQ.say(audio)
    DQ.runAndWait()
def time():
    time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(time)
def hour():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning,sir:")
    elif hour >= 12 and hour<18:
        speak("good evening,Sir:")
    else:
        speak("good afternoon,Sir:")
    speak("how can i help you:")
    #speak("what is your name :" )
def conmand():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language="EN")
        print("tony :"+ query)
    except sr.UnknownValueError:
        print(" Please repeat or typing the command")
        query=str( input('your order is:'))
    return query


if __name__ =="__main__":
    hour()
    while True:
        query=conmand().lower()
        if "google" in query:
            speak("what sould I search boss")
            search=conmand().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your { search }on google")

        if "youtube" in query:
            speak("what sould I search boss")
            search=conmand().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"here is your { search }on youtube")
        elif "open video" in query:

        elif "time" in query:
            time()
        elif "quit" in query:
            speak("goodbye sir")
        

