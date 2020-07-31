import speech_recognition

hear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("I'm listening")
    audio = hear.listen(mic)

try:
    you = hear.recognize_google(audio)
except:
    you = ""

print("you: ", you)
