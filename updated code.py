import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning mam !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon mam!")    
   
    else: 
        speak("Good Evening mam !")   
   
    assname =("ella") 
    speak("I am your Assistant") 
    speak(assname) 
      
  
def usrname(): 
    speak("What should i call you mam") 
    uname = takeCommand() 
    speak("Welcome ") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("".center(columns)) 
    print("Welcome Ms.", uname.center(columns)) 
    print("".center(columns)) 
      
    speak("How can i Help you, mam") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        speak("sorry ,i am unable to Recognizing your voice.")   
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close() 
if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear() 
    wishMe() 
    usrname() 
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            # music_dir = "G:\\Song" 
            music_dir = "C:\Users\Vasu\Music"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 

        elif 'whats the time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f" the time is {strTime}") 

        elif 'email to Eshika' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "Receiver email address"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whom should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by eshika.") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
        elif "calculate" in query:  
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
        elif"laugh ella" in query:
            speak("ha ha ha ha ha ha ha ")
  
        elif "why you came to world" in query: 
            speak("Thanks to Eshika. further It's a secret") 
        
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Gaurav") 
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Mister Gaurav ") 
  
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  0,  "Location of wallpaper", 0) 
            speak("Background changed succesfully") 
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop ella from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, mam") 
            note = takeCommand() 
            file = open('text.txt', 'w') 
            speak(" Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("text.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
        elif "update assistant" in query: 
            speak("After downloading file please replace this file with the downloaded one") 
            url = '# url after uploading file'
            r = requests.get(url, stream = True) 
              
            with open("Voice.py", "wb") as Pypdf: 
                  
                total_length = int(r.headers.get('content-length')) 
                  
                for ch in progress.bar(r.iter_content(chunk_size = 2391975), 
                                       expected_size =(total_length / 1024) + 1): 
                    if ch: 
                      Pypdf.write(ch) 
                      
        # NPPR9-FWDCX-D2C8J-H872K-2YT43 
        elif "ella" in query: 
              
            wishMe() 
            speak("ella is in your service Mam") 
            speak(assname) 
  
        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
              
        
  
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mam") 
            speak(assname) 
  
        # most asked question from google Assistant 
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
  
  