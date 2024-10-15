import pyautogui
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import win32gui
import win32con
import time





def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        r.adjust_for_ambient_noise(source) 
        
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def switch_to_new_incognito_tab():
    pyautogui.hotkey('ctrl','shift','n')
    time.sleep(2)
    
def new_window():
    pyautogui.hotkey('ctrl','n')
    time.sleep(2)
    
def new_tab():
    pyautogui.hotkey('ctrl','t')
    time.sleep(2)
    
def switch_between_tabs():
    # Press Ctrl + Tab to switch to the next tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    
def close_tab():

    # Press Ctrl + W to close the current tab
    pyautogui.hotkey('ctrl', 'w')

def close_app():

    # Press Alt + F4 to close the current window
    pyautogui.hotkey('alt', 'f4')