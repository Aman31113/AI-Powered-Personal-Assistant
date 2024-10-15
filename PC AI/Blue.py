# # agar pyaudio install nhi hai toh use
# # 1. pip intsall pipwin
# # 2. pip install pyaudio
# # or try 2. pipwin install pyaudio
 
    
    
# import pyttsx3
# import speech_recognition 
# import os
# import pyautogui
# import pygetwindow as gw
# import datetime
# import sounddevice as sd
# # import vosk
# import json
# import pyaudio
# # from vosk import Model,KaldiRecognizer
# from PyQt5 import QtWidgets,QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from blueUI import Ui_MainWindow


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# rate = engine.setProperty("rate",170)
# volume = engine.setProperty("volume",1000)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # def takeCommand():
# #     r = speech_recognition.Recognizer()
# #     with speech_recognition.Microphone() as source:
# #         print("Listening.....")
# #         r.pause_threshold = 1
# #         r.energy_threshold = 300
# #         audio = r.listen(source,0,3)
# #         r.adjust_for_ambient_noise(source) 

# #     try:
# #         print("Understanding..")
# #         query  = r.recognize_google(audio,language='en-in')
# #         print(f"You Said: {query}\n") 
# #     except Exception as e:
# #         print("Say that again")
# #         return "None"
# #     return query





# # import speech_recognition as sr

# # def listen_for_commands():
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening for commands...")

# #         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

# #         try:
# #             audio_data = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
# #             command = recognizer.recognize_google(audio_data)
# #             print("Command:", command)
# #         except sr.WaitTimeoutError:
# #             print("Timeout: No command detected.")
# #         except sr.UnknownValueError:
# #             print("Error: Unable to recognize speech.")
# #         except sr.RequestError as e:
# #             print(f"Error: {e}")

# # # Call the function to listen for commands through the Bluetooth microphone
# # listen_for_commands()







# # def close_application(query):
# #     try:
# #         os.system(f"taskkill /f /im {query}.exe")
# #         print(f"{query} closed successfully.")
# #         speak(f"{query} closed successfully.")
# #     except Exception as e:
# #         print(f"An error occurred while closing {query}: {e}")
# #         speak(f"An error occurred while closing {query}.")
        
        
# # def close_microsoft_edge():
# #     try:
# #         os.system("taskkill /f /im msedge")
# #         print("Microsoft Edge closed successfully.")
# #     except Exception as e:
# #         print(f"An error occurred while closing Microsoft Edge: {e}")
        
# # def close_file_explorer():
# #     try:
# #         os.system("taskkill /f /im explorer.exe")
# #         print("File Explorer windows closed successfully.")
# #     except Exception as e:
# #         print(f"An error occurred while closing File Explorer windows: {e}")
        
        
# def bring_to_foreground(query):
#     try:
#         # Use the hotkey combination Alt+Tab to cycle through open windows
#         pyautogui.hotkey('alt', 'tab')
#         # Type the name of the application to search for it in the window switcher
#         pyautogui.write(query)
#         # Press Enter to bring the application to the foreground
#         pyautogui.press('enter')
#         return True
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False
    

# def decrease_volume():
#     # Repeat pressing the volume down key 10 times to decrease by 10
#     for _ in range(5):
#         pyautogui.press('volumedown')
# def increase_volume():
#     # Repeat pressing the volume down key 10 times to decrease by 10
#     for _ in range(5):
#         pyautogui.press('volumeup')
        
        
        
# def save_conversation(conversation):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("conversation.txt", "a") as file:
#         file.write(f"{timestamp}: {conversation}\n")
        


# class MainThread(QThread):
#     def __int__(self):
#         super(MainThread,self).__inti__()
        
#     def run(self):
#         self.TaskExecution
        
#     def takeCommand(self):
#         r = speech_recognition.Recognizer()
#         with speech_recognition.Microphone() as source:
#             print("Listening.....")
#             r.pause_threshold = 1
#             r.energy_threshold = 300
#             audio = r.listen(source,0,3)
#             r.adjust_for_ambient_noise(source) 

#         try:
#             print("Understanding..")
#             query  = r.recognize_google(audio,language='en-in')
#             print(f"You Said: {query}\n")
#         except Exception as e:
#             print("Say that again")
#             return "None"
#         return query

#     def TaskExecution(self):
#         if __name__ == "__main__":
#             while True:
#                 self.query = self.takeCommand().lower()

#                 if "blue are you there" in self.query:
#                     from GreetMe import greetMe
#                     greetMe()
#                 elif "wake up blue" in self.query:
#                     from GreetMe import greetMe
#                     greetMe()
#                 elif "blue" in self.query:
#                     from GreetMe import greetMe
#                     greetMe()

#                     while True:
#                         self.query = self.takeCommand().lower()
#                         save_conversation(self.query)
#                         if "mute" in self.query:
#                             speak("Ok sir , You can call me anytime")
#                             break 
#                         elif "power off" in self.query:
#                             speak("okay sir , power off ")
#                             exit()
                        
#                         elif "hello" in self.query:
#                             speak("Hello sir, how are you ?")
#                         elif "i am fine" in self.query:
#                             speak("that's great, sir")
#                         elif "how are you" in self.query:
#                             speak("Perfect, sir")
#                         elif "thank you" in self.query:
#                             speak("you are welcome, sir")
                            
                            
#                         ####################################
#                         ####################################
#                         elif "google" in self.query:
#                             from Search import search_in_google
#                             search_in_google(self.query)
#                         # elif "Google" in self.query:
#                         #     from Search import searchGoogle
#                         #     searchGoogle(self.query)
#                         elif "youtube" in self.query:
#                             from Search import searchYoutube
#                             searchYoutube(self.query)
                            
                            
#                         ##################################
#                         ##################################
#                         elif "blue shut down" in self.query:
#                             os.system("shutdown /s /t 3")
#                         elif "blue shutdown" in self.query:
#                             os.system("shutdown /s /t 3")
#                         elif "restart" in self.query:
#                             os.system("shutdown /s /t 3")
#                         elif "blue restart laptop" in self.query:
#                             os.system("shutdown /r /t 3")
#                         elif "blue sleep mode on" in self.query:
#                             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                            
                            
#                             #############################################
#                         # elif "close" in self.query:
#                         #     self.query = self.query.replace("close","").strip()
#                         #     close_application(self.query)
#                         # elif "close Microsoft edge" in self.query:
#                         #     # self.query = self.query.replace("close","")
#                         #     close_microsoft_edge()
#                         # elif "close Explorer" in self.query:
#                         #     self.query = self.query.replace("close","") 
#                         #     close_file_explorer()
#                         elif self.query [:5].lower()=="close":
#                             import Close
#                             st=[self.query[5:]]
#                             Close.close(st[0])

                            
                            
                            
                            
#                             ###################################################
#                         elif "open" in self.query:
#                             self.query = self.query.replace("open","")
#                             self.query = self.query.replace("blue","")
#                             self.query = self.query.replace("blue open","")
                            
#                             pyautogui.press("super")
#                             pyautogui.typewrite(self.query)
#                             pyautogui.press("enter")
                            
                            
#                             ############################################
#                         elif "play" in self.query:
#                             pyautogui.press('playpause')
                            
#                         elif "pause" in self.query:
#                             pyautogui.press('playpause')
                            
#                         elif "next song"in self.query:
#                             pyautogui.press('nexttrack')
                            
#                         elif "previous song"in self.query:
#                             pyautogui.press('prevtrack')
                            
                            
#                         elif "increase volume"in self.query:
#                             # pyautogui.press('volumeup')
#                             increase_volume()
#                         elif "decrease volume"in self.query:
#                             # pyautogui.press('volumedown')
#                             decrease_volume()
                            
                        
#                             ########################################
#                         elif "change window" in self.query:
#                             self.query = self.query.replace("switch","")
#                             self.query = self.query.replace("switch to","")
#                             self.query = self.query.replace("switch ","")
#                             bring_to_foreground(self.query)
                            
                            
#                         elif "record in notepade" in self.query:
#                             self.query = self.query.replace("record this","")
#                             self.query = self.query.replace(" blue record this","")
#                             self.query = self.query.replace("record this","")
#                             from save import record_and_write_to_notepad
#                             record_and_write_to_notepad()
#                         elif "record in word file" in self.query:
#                             self.query = self.query.replace("record","")
#                             from save import record_and_write_to_word
#                             record_and_write_to_word()
                            
#                         elif "minimise current window" in self.query:
#                             self.query = self.query.replace("minimise","")
#                             from Minimize import minimize_current_window
#                             minimize_current_window()

                            
#                         elif "minimise all" in self.query:
#                             self.query = self.query.replace("minimise","")
#                             from Minimize import minimize_all_windows
#                             minimize_all_windows()
                            
#                         elif "incognito" in self.query:
#                             self.query= self.query.replace("blue","")
#                             from Switch import switch_to_new_incognito_tab
#                             switch_to_new_incognito_tab()
                            
#                         elif "new tab" in self.query:
#                             self.query= self.query.replace("blue","")
#                             self.query= self.query.replace("new","")
#                             from Switch import new_tab
#                             new_tab()
                            
#                         elif "new window" in self.query:
#                             self.query= self.query.replace("blue","")
#                             self.query= self.query.replace("new","")
#                             from Switch import new_window
#                             new_window()
                            
#                         elif "switch tab" in self.query:
#                             # self.query = self.query.replace("switch","")
#                             from Switch import switch_between_tabs
#                             switch_between_tabs()
                            
#                         elif "delete tab" in self.query:
#                             self.query = self.query.replace("close","")
#                             from Switch import close_tab
#                             close_tab()
                            
#                         elif "delete window" in self.query:
#                             self.query = self.query.replace("close","")
#                             from Switch import close_window
#                             close_window()




# class Main(QMainWindow):
#     def __inti__(self):
#         super().__inti__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.
        


import pyttsx3
import speech_recognition as sr
import os
import pyautogui
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow
from blueUI import Ui_MainWindow

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)
volume = engine.setProperty("volume", 1000)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def bring_to_foreground(query):
    try:
        pyautogui.hotkey('alt', 'tab')
        pyautogui.write(query)
        pyautogui.press('enter')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def decrease_volume():
    for _ in range(5):
        pyautogui.press('volumedown')

def increase_volume():
    for _ in range(5):
        pyautogui.press('volumeup')

def save_conversation(conversation):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("conversation.txt", "a") as file:
        file.write(f"{timestamp}: {conversation}\n")

class MainThread(QThread):
    def __init__(self, ui):
        super(MainThread, self).__init__()
        self.ui = ui

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, 0, 3)

        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query

    def TaskExecution(self):
        while True:
            self.query = self.takeCommand().lower()

            if "blue are you there" in self.query or "wake up blue" in self.query or "blue" in self.query:
                from GreetMe import greetMe
                greetMe()
                while True:
                    self.query = self.takeCommand().lower()
                    save_conversation(self.query)
                    self.ui.textBrowser.append(f"You: {self.query}")
                    if "mute" in self.query:
                        speak("Ok sir, You can call me anytime")
                        break
                    elif "power off" in self.query:
                        speak("Okay sir, power off")
                        QtWidgets.QApplication.quit()
                        return  # Exit the function to stop further execution
                    elif "hello" in self.query:
                        speak("Hello sir, how are you?")
                    elif "i am fine" in self.query:
                        speak("That's great, sir")
                    elif "how are you" in self.query:
                        speak("Perfect, sir")
                    elif "thank you" in self.query:
                        speak("You are welcome, sir")
                    elif "google" in self.query:
                        from Search import search_in_google
                        search_in_google(self.query)
                    elif "youtube" in self.query:
                        from Search import searchYoutube
                        searchYoutube(self.query)
                    elif "blue shut down" in self.query or "blue shutdown" in self.query:
                        os.system("shutdown /s /t 3")
                    elif "restart" in self.query or "blue restart laptop" in self.query:
                        os.system("shutdown /r /t 3")
                    elif "blue sleep mode on" in self.query:
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    # elif self.query[:5].lower() == "close":
                    #     import Close
                    #     st = [self.query[5:]]
                    #     Close.close(st[0])
                        
                    elif "open" in self.query:
                        self.query = self.query.replace("open", "").strip()
                        pyautogui.press("super")
                        pyautogui.typewrite(self.query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                    elif "play" in self.query or "pause" in self.query:
                        pyautogui.press('playpause')
                    elif "next song" in self.query:
                        pyautogui.press('nexttrack')
                    elif "previous song" in self.query:
                        pyautogui.press('prevtrack')
                    elif "increase volume" in self.query:
                        increase_volume()
                    elif "decrease volume" in self.query:
                        decrease_volume()
                    elif "change window" in self.query:
                        self.query = self.query.replace("switch", "").replace("switch to", "").replace("switch ", "")
                        bring_to_foreground(self.query)
                    elif "record in notepade" in self.query:
                        from save import record_and_write_to_notepad
                        record_and_write_to_notepad()
                    elif "record in word file" in self.query:
                        from save import record_and_write_to_word
                        record_and_write_to_word()
                    elif "minimise current window" in self.query:
                        from Minimize import minimize_current_window
                        minimize_current_window()
                    elif "minimise all" in self.query:
                        from Minimize import minimize_all_windows
                        minimize_all_windows()
                    elif "incognito" in self.query:
                        from Switch import switch_to_new_incognito_tab
                        switch_to_new_incognito_tab()
                    elif "new tab" in self.query:
                        from Switch import new_tab
                        new_tab()
                    elif "new window" in self.query:
                        from Switch import new_window
                        new_window()
                    elif "switch tab" in self.query:
                        from Switch import switch_between_tabs
                        switch_between_tabs()
                    elif "delete tab" in self.query:
                        from Switch import close_tab
                        close_tab()
                    elif "close" in self.query:
                        from Switch import close_app
                        close_app()
                        
                    # Append response to the QTextBrowser
                    self.ui.textBrowser.append(f"Blue: {self.query}")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startTask()
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/sgurp/Downloads/Artificial Intelligence design.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.thread = MainThread(self.ui)
        self.thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())




















# # import pyttsx3
# # import speech_recognition
# # import os
# # import pyautogui
# # import datetime
# # import openai
# # import pygetwindow as gw
# # import pyaudio

# # # Initialize pyttsx3
# # engine = pyttsx3.init("sapi5")
# # voices = engine.getProperty("voices")
# # engine.setProperty("voice", voices[0].id)
# # engine.setProperty("rate", 170)
# # engine.setProperty("volume", 1000)


# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()

# # def takeCommand():
# #     r = speech_recognition.Recognizer()
# #     with speech_recognition.Microphone() as source:
# #         print("Listening.....")
# #         r.pause_threshold = 1
# #         r.energy_threshold = 300
# #         r.adjust_for_ambient_noise(source)
# #         audio = r.listen(source, timeout=10, phrase_time_limit=10)

# #     try:
# #         print("Understanding..")
# #         self.query = r.recognize_google(audio, language='en-in')
# #         print(f"You Said: {self.query}\n")
# #     except Exception as e:
# #         print("Say that again")
# #         return "None"
# #     return self.query

# # def chat_with_gpt(prompt):
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[
# #             {"role": "system", "content": "You are a helpful assistant."},
# #             {"role": "user", "content": prompt}
# #         ],
# #         max_tokens=150,
# #         temperature=0.7,
# #     )
# #     return response.choices[0].message['content'].strip()

# # def bring_to_foreground(query):
# #     try:
# #         pyautogui.hotkey('alt', 'tab')
# #         pyautogui.write(query)
# #         pyautogui.press('enter')
# #         return True
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return False

# # def decrease_volume():
# #     for _ in range(5):
# #         pyautogui.press('volumedown')

# # def increase_volume():
# #     for _ in range(5):
# #         pyautogui.press('volumeup')

# # def save_conversation(conversation):
# #     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #     with open("conversation.txt", "a") as file:
# #         file.write(f"{timestamp}: {conversation}\n")

# # if __name__ == "__main__":
# #     while True:
# #         query = takeCommand().lower()

# #         if "blue are you there" in query or "wake up blue" in query or "blue" in query:
# #             from GreetMe import greetMe
# #             greetMe()

# #             while True:
# #                 query = takeCommand().lower()
# #                 save_conversation(query)
# #                 if "mute" in query:
# #                     speak("Ok sir, You can call me anytime")
# #                     break
# #                 elif "power off" in query:
# #                     speak("Okay sir, power off")
# #                     exit()
# #                 elif "hello" in query:
# #                     speak("Hello sir, how are you?")
# #                 elif "i am fine" in query:
# #                     speak("That's great, sir")
# #                 elif "how are you" in query:
# #                     speak("Perfect, sir")
# #                 elif "thank you" in query:
# #                     speak("You are welcome, sir")
# #                 elif "google" in query:
# #                     from Search import search_in_google
# #                     search_in_google(query)
# #                 elif "youtube" in query:
# #                     from Search import searchYoutube
# #                     searchYoutube(query)
# #                 elif "blue shut down" in query or "blue shutdown" in query:
# #                     os.system("shutdown /s /t 3")
# #                 elif "restart" in query or "blue restart laptop" in query:
# #                     os.system("shutdown /r /t 3")
# #                 elif "blue sleep mode on" in query:
# #                     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# #                 elif query[:5].lower() == "close":
# #                     import Close
# #                     st = [query[5:]]
# #                     Close.close(st[0])
# #                 elif "open" in query:
# #                     query = query.replace("open", "").strip()
# #                     pyautogui.press("super")
# #                     pyautogui.typewrite(query)
# #                     pyautogui.press("enter")
# #                 elif "play" in query:
# #                     pyautogui.press('playpause')
# #                 elif "pause" in query:
# #                     pyautogui.press('playpause')
# #                 elif "next song" in query:
# #                     pyautogui.press('nexttrack')
# #                 elif "previous song" in query:
# #                     pyautogui.press('prevtrack')
# #                 elif "increase volume" in query:
# #                     increase_volume()
# #                 elif "decrease volume" in query:
# #                     decrease_volume()
# #                 elif "change window" in query:
# #                     bring_to_foreground(query)
# #                 elif "record in notepad" in query:
# #                     from save import record_and_write_to_notepad
# #                     record_and_write_to_notepad()
# #                 elif "record in word file" in query:
# #                     from save import record_and_write_to_word
# #                     record_and_write_to_word()
# #                 elif "minimise current window" in query:
# #                     from Minimize import minimize_current_window
# #                     minimize_current_window()
# #                 elif "minimise all" in query:
# #                     from Minimize import minimize_all_windows
# #                     minimize_all_windows()
# #                 elif "incognito" in query:
# #                     from Switch import switch_to_new_incognito_tab
# #                     switch_to_new_incognito_tab()
# #                 elif "new tab" in query:
# #                     from Switch import new_tab
# #                     new_tab()
# #                 elif "new window" in query:
# #                     from Switch import new_window
# #                     new_window()
# #                 elif "switch tab" in query:
# #                     from Switch import switch_between_tabs
# #                     switch_between_tabs()
# #                 elif "delete tab" in query:
# #                     from Switch import close_tab
# #                     close_tab()
# #                 elif "delete window" in query:
# #                     from Switch import close_window
# #                     close_window()
# #                 elif "chat" in query:
# #                     user_query = query.replace("chat", "").strip()
# #                     response = chat_with_gpt(user_query)
# #                     speak(response)
# #                     save_conversation(f"ChatGPT: {response}")





# import pyttsx3
# import speech_recognition as sr
# import os
# import pyautogui
# import datetime
# import sounddevice as sd
# import pyaudio
# import wolframalpha

# # Initialize the speech engine
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 170)
# engine.setProperty("volume", 1000)



# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         r.energy_threshold = 300
#         audio = r.listen(source, 0, 3)
#         r.adjust_for_ambient_noise(source)

#     try:
#         print("Understanding..")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You Said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "None"
#     return query

# def wolfram_query(query):
#     try:
#         res = client.query(query)
#         answer = next(res.results).text
#         return answer
#     except Exception as e:
#         return "Sorry, I couldn't get an answer."

# # Other utility functions like bring_to_foreground, decrease_volume, increase_volume...

# if __name__ == "__main__":
#     while True:
#         query = takeCommand().lower()

#         if "blue are you there" in query:
#             from GreetMe import greetMe
#             greetMe()
#         elif "wake up blue" in query:
#             from GreetMe import greetMe
#             greetMe()
#         elif "blue" in query:
#             from GreetMe import greetMe
#             greetMe()

#             while True:
#                 query = takeCommand().lower()
#                 save_conversation(query)
#                 if "mute" in query:
#                     speak("Ok sir, You can call me anytime")
#                     break 
#                 elif "power off" in query:
#                     speak("okay sir, power off")
#                     exit()
#                 elif "hello" in query:
#                     speak("Hello sir, how are you?")
#                 elif "i am fine" in query:
#                     speak("that's great, sir")
#                 elif "how are you" in query:
#                     speak("Perfect, sir")
#                 elif "thank you" in query:
#                     speak("You are welcome, sir")

#                 # WolframAlpha Query Handling
#                 elif "calculate" in query or "what is" in query or "who is" in query:
#                     query = query.replace("calculate", "").replace("what is", "").replace("who is", "")
#                     answer = wolfram_query(query)
#                     speak(answer)

#                 # Other commands like opening apps, controlling volume, switching windows, etc.
