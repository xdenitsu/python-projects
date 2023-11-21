import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import random

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        return wikipedia.summary(query, sentences=3).lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def create_directory():
    try:
        speak("Sure! What should the name of the new directory be?")
        user_input = recognize_speech()
        os.mkdir(f'./{user_input}')
        speak(f"Directory '{user_input}' created successfully.")
    except Exception as e:
        speak(f"Sorry, I couldn't create a directory. {e}")

def shutdown_computer():
    try:
        speak("Sure! Shutting down your computer...")
        os.system('shutdown now')
    except Exception as e:
        speak(f"Sorry, I couldn't shutdown your computer. {e}")

def reboot_computer():
    try:
        speak("Sure! Rebooting your computer...")
        os.system('reboot')
    except Exception as e:
        speak(f"Sorry, I couldn't shutdown your computer. {e}")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def assist(command):
    if "hello" in command:
        speak("Hi there! How can I help?")
    elif "wiki" in command:
        speak("Sure thing! What would you like to know?")
        result = recognize_speech()
        speak(result)
    elif "create directory" in command:
        create_directory()
    elif "shutdown" in command:
        shutdown_computer()
    elif "random" in command:
        random_number = random.randint(1, 6)
        speak(f"Your random number between 1 and 6 is {random_number}")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm not sure how to respond to that. Please try again.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    while True:
        user_input = recognize_speech()
        assist(user_input)
