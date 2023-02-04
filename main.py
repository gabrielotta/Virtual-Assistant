from time import sleep
import speech_recognition as sr
import keyboard  
import va

recognizer = sr.Recognizer()

BOT_NAMES = []

def record_audio():
  with sr.Microphone() as source:
    audio = recognizer.listen(source, None, 3)
    voice_data = ''
    try:
      voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()
    except sr.UnknownValueError:
      print()
    except sr.RequestError:
      print('Serviço offline')

    print(">>", voice_data)
    for bot_name_variation in BOT_NAMES:
      if (bot_name_variation in voice_data):
        va.listen()
        break

while True:
  sleep(0.05) 
  if keyboard.is_pressed('F8'):
    print('ouvindo...')
    va.listen()
  sleep(0.05)