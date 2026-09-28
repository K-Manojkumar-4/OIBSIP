import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty( 'rate' , 170)

def speak(text):
    print("Assistant :" , text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening........")
        recognizer.adjust_for_ambient_noise(source , duration = 0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You Said :" , command )
        return command.lower()
    
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please say that again.")
        return ""
    
    except sr.RequestError:
        speak("Sorry, there is a problem with the speech service.")
        return ""

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%p")
    speak( f"The current time is {current_time}")

def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B:%d:%Y")

def search_web(query):
    speak( f"Searching the web for {query}")
    webbrowser.open("https://www.google.com/search?q={query}")

speak("Hello! I am your voice assistant. How can I help you?")

while True:
    command = listen()

    if command == "":
        continue

    if "hello" in command or "hi" in command:
        speak("Hello! How are you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "search" in command:
        topic = command.replace("search" , "")
        if topic:
            search_web(topic)
        else:
            speak("What would you like me to search for?")

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I can only respond to hello, time, date, or search commands right now.")

