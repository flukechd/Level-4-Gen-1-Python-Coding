import speech_recognition as sr
def SpeechToText(x):
    if x==1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print(source)
            print("start")
            # playsound("signal.mp3")
            audio = r.record(source, duration=5)  # บันทึกเสียง 5 วินาที
            # print(type(audio))#
            print("finish")

            # playsound("signal.mp3")
        # print(audio)
        try:
            text = r.recognize_google(audio, language = 'en')
            # print("None")
        except:
            text = "Try again please"
        return text
print(SpeechToText(1))
