import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
kevin = pyttsx3.init()

voices = kevin.getProperty('voices')
kevin.setProperty('voice', voices[0].id)

def talk(text):
    kevin.say(text)
    kevin.runAndWait()

def talking():
    try:
        with sr.Microphone() as source:
            print ("You can talk now...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "kevin" in command:
                command = command.replace('kevin', '')
                print (command)
    except:
        pass
    return command 

def run_talk():
    cmd = talking()
    print(cmd)
    if 'play' in cmd:
        play = cmd.replace('play', '')
        talk('playing' + play)
        print('playing' + play)
        pywhatkit.playonyt(play )
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is' + time)
        print(time)
    elif 'who' or 'what' or "give" or 'find' or 'can' in cmd:
        search = cmd.replace('who' or 'what' or "give" or 'find' or 'can', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
        
        
run_talk()