import pyttsx3
import speech_recognition

#init
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
    # listen
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: ", you)
    you = "hello"
    if "hello" in you:
        robot_brain = "hello"
    elif "bye" in you:
        robot_brain = "Bye Hill Rose"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thanks"
    print("Robot", robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()