import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime
import time

r = sr.Recognizer()


def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1] .id)
    engine.say(command)
    engine.runAndWait()

#OLD VERSION

# def commands():
#     try:
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             print('Listen...Ask...Now')
#             audioin = r.listen(source)
#             my_text = r.recognize_google(audioin)
#             my_text = my_text.lower()
#             print(my_text)

#             if 'play' in my_text:
#                 my_text = my_text.replace('play', '')
#                 speak('playing' + my_text)
#                 pywhatkit.playonyt(my_text)

#             elif 'tell me about' in my_text:
#                 subject = my_text.replace('tell me about', '')
#                 info = wikipedia.summary(subject, 1)
#                 speak(info)

#             elif 'time' in my_text:
#                 timenow = datetime.datetime.now().strftime('%H:%M')
#                 speak(timenow)

#             else:
#                 speak('Please ask properly...')

#     except:
#         print('Please ask again..')

# commands()

#UPDATED VERSION

#make all feature as a function for more efficiency
def playYT(inputs):
    inputs = inputs.replace('play', '')
    speak('playing' + inputs)
    pywhatkit.playonyt(inputs)

def google(inputs):
    subject = inputs.replace('tell me about', '')
    speak('searching' + subject)
    pywhatkit.search(subject)

def tellTime():
    timenow = datetime.datetime.now().strftime('%H:%M')
    speak(timenow)

def bingChilling():
    url = "https://youtube.com/shorts/AWOyEIuVzzQ?feature=share"
    pywhatkit.playonyt(url)

#give a clear list of all audio devices connected with your device   
print("List of all audio devices connected to your device\n")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


print("\ndevice_index=1 (probably your default audio input) will be used for recording")
time.sleep(5)
os.system('cls')

print("Hi! I'm your private voice assitant!")

while True:
    
    try:
        #sr.Microphone will use yor default microphone so check what is your default mic. To change microphone edit sr.Microphone(device_index=[devices index number according on the previous list])
        with sr.Microphone() as mic: 
                r.adjust_for_ambient_noise(mic)
                print('Listening...')
                audioin = r.listen(mic)
                my_text = r.recognize_google(audioin)
                my_text = my_text.lower()
                

                if 'play' in my_text:
                    playYT(my_text)
                    

                elif 'tell me about' in my_text:
                    google(my_text)
                    

                elif 'time' in my_text:
                    tellTime()
                    

                elif 'close' in my_text or 'bye' in my_text:
                    speak("Good bye, see you next time!")
                    break

                elif 'ice cream' in my_text:
                    bingChilling()

                else:
                    print("You said", my_text)
                print("clearing screen...")
                time.sleep(3)
                os.system('cls')
                continue

    #error handling if there is no input               
    except:
        r = sr.Recognizer()
        os.system('cls')
        continue

#CHANGE LOG
# Added some feature:
#     1. auto loop
#     2. system exit on voice command
#     3. some jokes
#     4. error handling
# Guide to install all modules:
#     1. Open terminal in visual studio
#     2. type "py -m pip install -r modules.txt"
  
           
