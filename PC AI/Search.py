# import pywhatkit
# import wikipedia
# import pyttsx3
# import speech_recognition as sr
# import webbrowser


# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         # print("\n")
#         r.pause_threshold = 1
#         r.energy_threshold = 250
#         audio = r.listen(source,0,5)
        
#     try:
#         # print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}\n")

#     except Exception as e:
#         speak("Say that again place...")
#         return "none"
#     return query
    
    
# query = takeCommand().lower()

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices',voices[0].id)
# engine.setProperty('rate',180)


# #text to speech
# def speak(audio):
#     engine.say(audio)
#     #############
#     print(audio)
#     ##################
#     engine.runAndWait()
    
# def searchGoogle(query):
#     if"google" in query:
#         import wikipedia as googleScrap
#         query = query.replace("blue","")
#         query = query.replace("google search","")
#         query = query.replace("google","")
#         # web =  "https://www.google.com/search?q=" + query
#         # webbrowser.open(web)
#         # pywhatkit.serach(query)
#         speak("this is i found on google")
        
#     try:
#         pywhatkit.search(query)
#         result = googleScrap.summary(query,1)
#         speak(result)
        
#     except:
#         speak("Found nothing to spaek")
        
        
# def searchYoutube(query):
#     if"youtube" in query:
#         speak(" this is found on youtube!")
#         query = query.replace("youtube","")
#         query = query.replace("blue","")
#         query = query.replace("youtube search","")
#         query = query.replace("search on youtube","")
#         web = "https://www.youtube.com/results?search_query=" + query
#         webbrowser.open(web)
#         pywhatkit.playonyt(query)
#         speak("Done, sir")
        
        
        
        
import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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

# def searchGoogle(query):
#     if "google" in query:
#         import wikipedia as googleScrap
#         query = query.replace("blue","")
#         query = query.replace("google search","")
#         query = query.replace("google","")
#         speak("This is what I found on google")

#         try:
#             pywhatkit.search(query)
#             result = googleScrap.summary(query,1)
#             speak(result)

#         except:
#             speak("No speakable output available")

def search_in_google(query):    
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(search_url)

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("blue","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
        
        
