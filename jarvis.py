import pyttsx3
import datetime
import speech_recognition as sr
# pip install speechRecognition
import wikipedia, webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish me Function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mr.Vohera")
        speak("I am Jarvis. Have a nice day.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr.Vohera")
        speak("I am Jarvis. Have a nice noon.")
    else:
        speak("Good Evening Mr.Vohera")
        speak("I am Jarvis. Have a nice night.")

    


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        print("E1 ")
        #r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        print("E2")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        speak(query)
        print(f"User said: {query}\n")  # User query will be printed.


    except Exception as e:
        print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while(True):
        query = takecommand().lower()
    # logic for executing tasks
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            break

        elif 'open youtube' in query:
            webbrowser.get('open -a C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s')
            query = query.replace('open youtube', '')
            webbrowser.open(f'youtube.com/{query}')
            break
        else:
            break
