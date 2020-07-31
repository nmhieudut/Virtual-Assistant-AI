import pyttsx3

sentence = "Hello everyone today i feel so good"

engine = pyttsx3.init()
engine.say(sentence)
engine.runAndWait()