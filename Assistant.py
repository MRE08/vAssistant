#Import the speech recognition module
import speech_recognition as sr 

#Import Wikipedia for searches
import wikipedia
#Import text to speech mode
import pyttsx3

#Import Whatkit module
import pywhatkit

#Import Time Module
import datetime
#creating a listener
listener = sr.Recognizer()

#creating a talk back engine and initializing it 
engine = pyttsx3.init()
engine.setProperty('rate', 200)

#Greeting to gather user's name
firstGreet = 'Welcome. What can I call you?'

#Definining the Listening function
def listening():
    #Setting the source as microphone
    with sr.Microphone() as source:
        print('...Listening')
        #making the voice variable global
        global voice
        #voice calls the listener
        voice = listener.listen(source)
        #Return this information
        return

#Defining the speaking function
def engineSpeak(text):
    engine.say(text)
    engine.runAndWait()

#making engine gather user's name
#RunandWait statement is important so it will run and wait for other part of the code to run
print(firstGreet)
engineSpeak(firstGreet)

#listening for answer
listening()
#Creating a try block
try:
    #describing username variable for user's name
    userName = listener.recognize_google(voice)

    #Engine's response after taking user's name
    answer= 'Welcome' ',' + userName
    engine.say(answer)
    print('Welcome' , userName)
    #Using a try function incase the code fails
    #Ask for a command from user
    engineSpeak('How can I be of help to you?')
    #listening()

    #Telling the listener to listen0
    #command = listener.recognize_google(voice)
    #Enclosing everything in a function to make it easy to loop
    def secTrial():
        engineSpeak('Do you want to me to do anything else?')
        listening()
        newJob = listener.recognize_google(voice)
        if 'no' in newJob:
            engineSpeak('Okay. Goodbye baby')
            pass
        elif 'yes' in newJob:
            engineSpeak('That\'s fine. Let us go over it again')
            response()

    def response():
        listening()
        command = listener.recognize_google(voice)
        command = command.replace('can you', '')
        if 'play' and 'by' in command:
            command = command.replace('play','')
            musicRP = 'Alright!. Playing','', command
            engineSpeak(musicRP)
            pywhatkit.playonyt(command)
        elif 'what' and 'time' in command:
            time = datetime.datetime.now().strftime('%I %M %p')
            engineSpeak('The time is' + time)
            print(time)
        elif 'do' and  'love me' in command:
            print('Sorry. I am already in a serious relationship!')
            engineSpeak('Sorry. I am already in a serious relationship!')
        elif 'Who'in command or 'where' in command or 'what' in command:
            info = command.replace('can you tell me about', '')
            engineSpeak('Here is what I found')
            pywhatkit.search(info)   
        elif 'go on a date' in command:
            engineSpeak('Oh. I\'m sorry. I do not think I will have time for that')
            print('Oh. I\'m sorry. I do not think I will have time for that')
        elif 'say my name' in command:
            global sayName
            sayName = 'That is easy. Your name is','',userName
            engineSpeak(sayName)
        else:
            engineSpeak('Sorry. I am too stupid to carry out that operation')
        secTrial()
    response()
    
#This will run if the try block cannot
except: 
    errorMsg='Sorry!. I can not process your request because there is an error. Confirm you have your internet on and try again!'
    print(errorMsg)
    engineSpeak(errorMsg)
    pass