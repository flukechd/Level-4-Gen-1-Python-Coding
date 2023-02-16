import speech_recognition as sr
import pyaudio
# create a recognizer object
r = sr.Recognizer()

# get audio from the microphone
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

# recognize the speech
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Error requesting results from Google Speech Recognition service: {0}".format(e))