from gtts import gTTS
import os

while True:
    text = input("Enter the text you want to convert to speech (enter 'quit' to exit): ")

    if text.lower() == "quit":
        break

    tts = gTTS(text=text, lang="en")
    tts.save("hello.mp3")

    os.system("hello.mp3")