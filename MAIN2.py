import pyttsx3
import pyaudio
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import random
import pywhatkit as pt
from boltiot import Bolt
from tkinter import *
import threading
import pyautogui

y="Nishant"


# FOR GUI
main = Tk()
main.geometry("620x900")
main.title("ASSISTANT_NIRA")
main.configure(background="#000000")
img = PhotoImage(file="bt1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

# FOR SPEAK FUNCTION
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


flag = 0


def Wishme():
    global y
    y = Name()

    p, q, u = "Good Morning", "Good Afternoon", "Good Evenening"
    hour = int(datetime.datetime.now().hour)
    if (hour >= 6 and hour < 12):
        msg.insert(END,"NIRA: " + p + " " + y + " How can I help you?")
        speak(p + " " + y + " How can I help you?")
    elif (hour >= 12 and hour < 18):
        msg.insert(END,"NIRA: "+q + " " + y + " How can I help you?")
        speak(q + " " + y + " How can I help you?")
    else:
        msg.insert(END,"NIRA: " +u + " " + y + " How can I help you?")
        speak(u + " " + y + " How can I help you?")


def takeCommand():
    # It takes Microphone input from user and  returns string output
    global flag
    r = sr.Recognizer()
    r.energy_threshold = 500
    with sr.Microphone() as m:
        msg.insert(END,"NIRA: Listening...")
        audio = r.listen(m)
    try:
        msg.insert(END,"NIRA: Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        msg.insert(END,"You: " + query)
        flag = 1
        return query
    except Exception as e:
        msg.insert(END,"NIRA: Say that again please!")


def Name():
    global flag
    msg.insert(END,"NIRA: Hey I am Nira your virtual assistant! Please tell me your name Sir!")
    speak("Hey I am Nira your virtual assistant! Please tell me your name Sir!")
    while (flag == 0):
        x = takeCommand()
    flag = 0
    return x


def exit1():
    global y
    msg.insert(END,"NIRA: Gudbye " + y + " I loook forward to our next meeting!")
    speak("Gudbye " + y + " I loook forward to our next meeting")
    exit()


def query1():
    global flag
    while (flag == 0):
        m = takeCommand()
    flag = 0
    return m


def date():
    a = str(datetime.datetime.now().day)
    b = str(datetime.datetime.now().year)
    c = datetime.datetime.now()
    d = c.strftime("%B")
    e = a + " " + d + " " + b
    msg.insert(END,"NIRA: " +e)
    speak("Sir the time is" +e)


def Sending_Whatsapp_Message():
    global flag
    Rohan = "+919793310609"
    a = datetime.datetime.now().hour
    b = datetime.datetime.now().minute
    msg.insert(END,"NIRA: Speak Message")
    speak("Speak Message")
    while flag == 0:
        y = takeCommand()
    flag = 0
    pt.sendwhatmsg(Rohan, y, a, b + 1)
    msg.insert(END,"NIRA: Your message has been sent")
    speak("Your message has been sent!")


def Switching_Light_On():
    api_key = "179e93cd-958b-467a-8c94-8a83f568c7c5"
    device_id = "BOLT1115545"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalWrite('0', "HIGH")
    a="Your LED is switched on"
    msg.insert(END,"NIRA: " + a)
    speak(a)
    print(response)

def TakeScreenshot():
    with open("screenshot.txt", "r") as f:
        v = f.read()
    v=int(v)+1
    pyautogui.screenshot('C:\\Users\\KIIT\\Desktop\\SS\\image' + str(v) +'.png')
    with open("screenshot.txt", "w") as f:
        f.write(str(v))
    print("Done")

def Controlling_Light_Intensity():
    global flag
    msg.insert(END,"NIRA: Choose the intensity between 0 to 255")
    speak("Choose the intensity between 0 to 255")
    while flag==0:
        x=takeCommand()
    flag=0
    api_key = "179e93cd-958b-467a-8c94-8a83f568c7c5"
    device_id = "BOLT1115545"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.analogWrite(0,x)
    a="Your LED intensity has been changed!"
    msg.insert(END,"NIRA: " + a)
    speak(a)
    print(response)

def Switching_Buzzer_On():
    api_key = "179e93cd-958b-467a-8c94-8a83f568c7c5"
    device_id = "BOLT1115545"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalWrite('1', "HIGH")
    a="Your Buzzer is switched on"
    msg.insert(END,"NIRA: " + a)
    speak(a)
    print(response)

def Switching_Buzzer_Off():
    api_key = "179e93cd-958b-467a-8c94-8a83f568c7c5"
    device_id = "BOLT1115545"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalWrite('1', "LOW")
    a = "Your Buzzer has been switched off"
    msg.insert(END, "NIRA :" + a)
    speak(a)
    print(response)




def Switching_Light_Off():
    api_key = "179e93cd-958b-467a-8c94-8a83f568c7c5"
    device_id = "BOLT1115545"
    mybolt = Bolt(api_key, device_id)
    response = mybolt.digitalWrite('0', "LOW")
    a = "Your LED is switched off"
    msg.insert(END, "NIRA :" + a)
    speak(a)
    print(response)





def Main():

    Wishme()
    while True:
        query = query1()
        query = query.lower()

        # Logic for executing task based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            msg.insert(END,results)
            speak(results)
        elif 'bye' in query:
            exit1()
        elif ' youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif ' music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            n = random.randint(0, len(songs) - 1)
            speak(f"Playing {songs[n]}")
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            msg.insert(END,strTime)
            speak(f"Sir the time is {strTime}")

        elif 'watch' in query:
            a = query.split()
            b = str(a[-1])
            pt.playonyt(b)


        elif 'cancel' in query:
            msg.insert(END,"NIRA: Scheduled shutdown is cancelled!")
            speak("Scheduled shutdown is cancelled!")
            pt.cancelShutdown()

        elif 'shut' in query:
            msg.insert(END,"Your PC will shut down in 50 second")
            speak("your PC will shut down in 50 second")
            pt.shutdown(50)





        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open("https://www." + query + ".com/")

        elif 'jumbled' in query:
            path = "C:\\Users\\KIIT\\PycharmProjects\\Jumbled\\Game1.exe"
            os.startfile(path)


        elif "how are you " in query:
            msg.insert(END,"I am doing Great!")
            speak("I am doing Great")


        elif "date" in query:
            date()

        elif "whatsapp" in query:
            Sending_Whatsapp_Message()



        elif "on" in query:
            Switching_Light_On()

        elif "me" in query:
            Switching_Buzzer_On()

        elif 'intensity' in query:
            Controlling_Light_Intensity()

        elif "off" in query:
            Switching_Light_Off()



        elif "am" in query:
            Switching_Buzzer_Off()





        elif "screenshot" in query:
            speak("Doing")
            TakeScreenshot()
            msg.insert(END,"Done")
            speak("Done")


        else:
            continue


frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=15, yscrollcommand=sc.set,)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=RIGHT, fill=BOTH, pady=10)
frame.pack()


def repeatL():
    try:
        Main()
    except Exception as e:
        print (e)
        print("Bye")

t=threading.Thread(target=repeatL)
t.start()
main.mainloop()
















