import pyautogui
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import win32gui
import win32con





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

# def minimize_current_window():
#     """
#     Minimize the current active window.
#     """
#     pyautogui.hotkey('win', 'down')

# # Call the function to minimize the current window





def minimize_all_windows():
    """
    Minimize all open windows.
    """
    pyautogui.hotkey('win', 'd')

# Call the function to minimize all windows


def minimize_current_window():
    """
    Minimize the current active window.
    """
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
