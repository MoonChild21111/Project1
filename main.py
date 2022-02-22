import speech_recognition  # speech recognition library
import pyttsx3  # python text to speech version 3
import pywhatkit  # used for youtube function  # used for current time telling
import wikipedia  # used to search wikipedia for stuff
from playsound import playsound
from datetime import datetime
from datetime import timedelta
listener = speech_recognition.Recognizer()  # creating a recognizer for out voice


def speak(words):  # alex speak function
    bol = pyttsx3.init()  # initializing the pyttsx3
    bol.say(words)
    bol.runAndWait()


speak("Hi. My name is Alex. How can I help you?")


def listening_to_me():
    try:  # for check of error or any other situation
        with speech_recognition.Microphone() as source:  # exception handling
            print("Speak now...")
            voice = listener.listen(source, 10, 3)
            command = listener.recognize_google(voice)  # uses google API to turn from voice to text
            command = command.lower()  # command in lowercase to check for certain string
            if 'alexa' in command:  # if call Alexa rather than Alex
                command = command.replace("alexa", "") # removes word Alexa from command
                speak("My name is Alex, not Alexa. I am literally a dude.")
            if 'alex' in command:  # removes the word alex from command
                command = command.replace("alex", "")
    except:  # python does not do anything because of pass
        pass
    return command


strTime = int(datetime.now().strftime("%H"))  # will be used in time in the coming code
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))  # adds 2 mins to current time for sending msg


def all_features():  # function for all features
    command = listening_to_me()  # calling above function
    print(command)
    if 'play' in command:  # plays youtube video if user says play
        music = command.replace("play", "")  # to remove word play from youtube search
        speak(f'Ok. Playing {music}')
        print(f'Ok. Playing {music}')
        pywhatkit.playonyt(music)  # function to play youtube video
    elif 'time' in command:  # tells time
        time = datetime.now().strftime('%H:%M')  # current time in hh:mm format
        print(time)
        speak(f"The current time is {time}")  # says the time
    elif 'tell me about' in command:  # shows wikipedia article
        thing = command.replace("tell me about", '')  # removes the unwanted text from query
        search = wikipedia.summary(thing, 2)  # provides summary of information in 2 lines
        print(search)
        speak(search) # says the search
    elif 'joke' in command:  # tells a joke
        speak("hahaha Your life")
        print("Your life.")
    elif "hello" in command:  # just a mini question
        speak("Hi, how are you?")
        command = listening_to_me()
        if "i am fine" in command:
            speak("That sounds like a lie but ok")
        elif "how are you" in command:
            speak("I am perfect as always, unlike a certain someone.")
    elif 'send a message' in command:  # for whatsapp message sending
        speak("Who do you want to send the message to")
        a = int(input('For Rameen Amir, press 1 -- For Shalina Riaz, press 2: '))  # takes who to send message to
        if a == 1:
            speak("Whats the message")
            message = str(input("Enter the message:  "))
            pywhatkit.sendwhatmsg("+923481694445", message, time_hour=strTime, time_min=update)
        elif a == 2:
            speak("Whats the message")
            message = str(input("Enter the message:  "))
            pywhatkit.sendwhatmsg("+923438811028", message, time_hour=strTime, time_min=update)
        else:
            pass
    elif 'alarm' in command:  # sets an alarm
        speak("What time should the alarm ring...")
        command2 = listening_to_me()
        print(command2)
        while True:
            time_a = datetime.datetime.now()  # current time
            now = time_a.strftime('%I:%M:%p')  # puts time in now
            print(now)

            now == command2  # equal to current time
            speak("Time to wake up...")
            playsound('Alarm.mp3')  # ringtone
            speak("Alarm Closed")
            break
    else:  # if alex does not understand
        speak("please say the command again...")
        print("please say the command again...")

while True:
    all_features()  # calling features function


