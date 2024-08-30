import os
import openai
from playsound import playsound
import time
import pyttsx3
# import speech_recognition as sr

import backstories

# Backstory


bst = int(input('''Choose From The List Of Backstory :_ \n
[0] : Normal Mode
[1] : Hitler
[2] : Omega
[3] : Marv
[4] : AI
'''))


b = "Human : "

if bst == 0:
  backstory = ''
  b = ''
elif bst == 1:
    backstory = backstories.Hitler
elif bst == 2:
    backstory = backstories.Omega
elif bst == 3:
    backstory = backstories.Marv
elif bst == 4:
    backstory = backstories.AI





# Setting Up Voice Engine -->

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Load your API key from an environment variable or secret management service
openai.api_key = "oepnai_key"

print("Starting AI Please Wait ...... ")
playsound('videoplayback.wav')

time.sleep(.5)
speak("Hey There , How are you Doing Today")






# Main Line --->

while True:

  user_input = input(": ")
  if user_input == "quit" or user_input == "exit":
    speak("Exiting")
    exit()

  response = openai.Completion.create(model="text-davinci-002",
                                      prompt=backstory + b + user_input,
                                      temperature=0,
                                      max_tokens=256)

  res = response['choices'][0]['text']

  print(res)
  speak(res)