# Author : Patel Riyank 
# Date : 13 December 2020 

#************** JARVIS PERSONAL DESKTOP ASSISTANT ***********************#

import pyttsx3    # used  for conversion of text to speech , install using 'pip install pyttsx3'
import speech_recognition as sr  # used for recognition of speech , install using 'pip install speechRecognition'
import wikipedia # used for getting wikipedia of the persons, install using 'pip install wikipedia'
import webbrowser 
import os 
import ctypes
import pyjokes
import time
import random
import functions as fnc
from PyDictionary import PyDictionary

# Getting Voices from the pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)  # setting the voice ,Set 0 for Male and 1 for Female voice
engine.setProperty("language",'hi')

def speak(audio):
    '''
    This function can take some string input to covert it into audio
    '''
    engine.say(audio)
    engine.runAndWait()
 
def takeCommand():
    '''
    This function takes the microphone input and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:        # this microphone cannot work if pyaudio is not install 
        r.pause_threshold = 1    # increasing the pause threshold to 1s from 0.8 so that it can detect audio till 1s space
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")

    except Exception as e :
        # print(e)
        print("Say that again please...")
        return "None"
    return query  # it is returning the string which is coverted from audio 

if __name__ == "__main__":
    '''
    Main Function
    '''
    crkPass = False
    fnc.wishMe()
    speak("Please tell me password once!")
    pswrd = takeCommand().lower().replace(" ","")
    crkPass = fnc.checkPassword(pswrd)
    if crkPass :
        speak("Password Matched")
        speak("Jarvis 2 point o is in your service")
        speak("How may i help you?")

    while crkPass :
        query = takeCommand().lower()

        #Logic for recognizing tasks based on query
        if 'who are you' in query:
            speak("I am Jarvis! ,Personal Virtual Assistant of Riyank Sir")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Riyank.")

        elif "who am i" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Riyank. further It's a secret")

        elif 'joke' in query:
            print(pyjokes.get_joke())

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif "don't listen" in query or "stop listening" in query or "take rest" in query:
            speak("In how much time i will meet again?")
            a = int(takeCommand())
            speak(f"Ok i will meet you in {a} seconds")
            time.sleep(a)
            speak("I am back riyank")

        elif ("update" in query or "change" in query) and "password" in query:
            speak("Please tell me the previous password")
            prpass = takeCommand().lower()
            mchPassword = fnc.checkPassword(prpass)
            if mchPassword :
                speak("Please tell me the new password riyank")
                nwPassword = takeCommand().lower().replace(" ","")
                speak("Please tell me the new password once again")
                nwoPassword = takeCommand().lower().replace(" ","")
                if nwPassword == nwoPassword:
                    fnc.setPassword(nwoPassword)
                    speak("Ok i remembered the new password,don't worry riyank")
                else:
                    speak("Sorry the password is not matched!")
            else :
                speak("The password is incorrect! Please try again")
            
        # command  for searching in wikipedia
        elif 'wikipedia' in query:  
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            try:      
                results = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia ")
                print(results)
            except:
                speak(results)
                speak(f"Wikipedia of {query} not found")

        # commands  for searching in browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open flow' in query:
            webbrowser.open("stackoverflow.com")

        # #####################################

        # # open  sowftware
        elif 'open code' in query :
            codePath = '"C:\\Users\\Riyank\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = fnc.datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Riyank, the time is {strTime}')
        elif 'the date' in query:
            strTime = fnc.datetime.datetime.now().strftime("%D")
            speak(f'Riyank, the date is {strTime}')

        elif ('email' in query or 'mail' in query) and 'send' in query:
            try :
                if 'to' in query:
                    query=query.replace(' ',"")
                    findMail = query.partition('to')[2]
                    to = findMail
                    speak("What should I say!")
                    content = takeCommand()
                    print("Sending mail...")
                    fnc.sendEmail(to,content)
                    print("Email has been sent!")
                    speak("Email has been sent!")
                else :
                    speak("To whom i send mail?")
                    to = takeCommand().lower().strip()
                    speak("What should I say!")
                    content = takeCommand()
                    print("Sending mail...")
                    fnc.sendEmail(to,content)
                    print("Email has been sent!")
                    speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir , I am unable to send this email")

        elif ('add' in query or 'save' in query or 'remember' in query) and 'email' in query:
            speak('What is the email address?')
            emailAddress = takeCommand().lower().replace(" ","")
            speak("whos email is this?")
            person = takeCommand()
            fnc.saveEmail(emailAddress,person)
            speak("Ok, i remembered the email, don't worry riyank")

        elif 'whatsapp' in query and ('send' in query or 'do' in query) :
            if 'to' in query:
                query=query.replace(' ',"")
                findNum = query.partition('to')[2]
                to = findNum
                speak("Ok,what message should i send?")
                msg=takeCommand().strip()
                fnc.sendMsgWhatsapp(to,msg)
            else:
                speak("To whom i should send message?")
                person = takeCommand().lower().strip()
                speak("Ok,what message should i send?")
                msg=takeCommand().strip()
                fnc.sendMsgWhatsapp(person,msg)

        elif ('add' in query or 'save' in query  or 'remember' in query) and ('phone' in query or 'mobile' in query):
            speak("Tell me the number")
            number = takeCommand().replace(" ","")
            speak("For whom i save this number")
            person = takeCommand().lower()
            fnc.savePhoneNumber(person,number)
            speak("Ok, i remembered the number, don't worry riyank")

        elif  'play music' in query or 'play song' in query:
            music_dir = "D:\\Music"          # it is the dir location where all the musics stored.
            songs=os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            speak("Ya sure, I am playing your favourite music")
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'quit' in query or 'close' in query:
            exit()