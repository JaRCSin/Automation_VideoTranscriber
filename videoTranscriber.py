#%%
#==========================
#   Video  Transcriber
#==========================
# syntax in this file will be used in the VirtualHuman Project in the Future

# Please Install these libraries 
# Install something to grab you video -- you can use your personal video in DIR
# pip install youtube-dl
    # when downloading a video in youtube: [youtube-dl "URL" --recode-video mkv]
# pip install ibm_watson

#%% Importing Libraries

import subprocess as sp
import speech_recognition as sr
import pyttsx3 as pytt
#%% Extract Audio
command = 'ffmpeg -i video2.mkv -ab 160k -ar 44100 -vn audio.wav'
sp.call(command, shell=True)

#%% Speech to text

r = sr.Recognizer()
wav = sr.AudioFile('audio.wav')

with wav as source:
    audio = r.record(source)
text = r.recognize_google(audio)



#%% Write in text file

text_file = open('D:/JohnDocuments/10_Data_AI_ML/02_AutoTranscriber/Video_Transcriber/TranscriptedText.txt','w')
n = text_file.write(text)
text_file.close()
print('.')
print('.')
print('.')
print('.')


#%% Text to Speech
# this is just for testing the text
engine = pytt.init()
# Setting Voices 
voices = engine.getProperty("voices")
#----------------
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) # speed
engine.say(text)
engine.runAndWait()
