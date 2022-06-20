import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    print("I am alexa. Please tell me how may i help you🤩🤩")
    speak("I am alexa. Please tell me how may i help you")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"Boss said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saajosaam@gmail.com','Demo@1998')
    server.sendmail('saajosaam@gmail.com',to,content)
    server.close()


if __name__ == '__main__':

    wishMe()

    while True:
        query=takeCommand().lower()
        if 'info about' in query:
            try:
                speak("Searching...")
                query=query.replace("info about","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry boss.. Did not find anything")
            

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        
        
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
            print(strtime)

        elif 'code' in query:
            codePath="C:\\Users\\sajos\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("opening Vs Code")
            os.startfile(codePath)
        
        elif 'joke' in query:
            s=pyjokes.get_joke()
            print(s)
            speak(s)

        elif 'open chrome' in query:
            path="C:\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        

        elif 'mail to myself' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="zajozamambalakara@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")
        
        elif 'play video' in query:
            speak("What should I play?")
            content=takeCommand()
            pywhatkit.playonyt(content)
            speak("Video has been played")
        
        
        elif 'stop music' in query:
            pywhatkit.stop()
            speak("Music has been stopped")
        
        elif 'stop video' in query:
            pywhatkit.stop()
            speak("Video has been stopped")
        
        elif 'shutdown' in query:
            speak("Boss is shutting down")
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            speak("Boss is restarting")
            os.system("shutdown /r /t 1")
        
        elif 'logout' in query:
            speak("Boss is logging out")
            os.system("shutdown /l /t 1")
        
        elif 'exit' in query:
            speak("Bye Sir. Have a good day")
            print("Bye")
            exit()
        else:
            speak("I don't know what you said")
            print("I don't know what you said")
            


    