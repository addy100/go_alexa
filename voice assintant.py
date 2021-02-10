#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import pyttsx3


# In[5]:


listener = sr.Recognizer()
speaker = pyttsx3.init()
speaker.say('Hi!')
speaker.say('How can I help you?')
speaker.runAndWait()

## to give a different voice
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
speaker.say('I a your mate!')

try:
    with sr.Microphone() as source:
        print ('Listening')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        command = command.lower()
        if 'alexa' in command:
            print ('Hi! here I am')
            
except:
    pass

