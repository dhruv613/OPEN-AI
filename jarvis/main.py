import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()  
engine = pyttsx3.init()

# Converts text to speech.
def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

        # Listens to the microphone and recognizes speech.
def listen_and_recognize():
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust to background noise
        audio = recognizer.listen(source, phrase_time_limit=2)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        speak(f"Could not connect to the internet. Error: {e}")
        return None



if __name__ == "__main__":
    speak("Hello, I am Jarvis")
    
    active = False
    
    while True:
        
        if not active:
            print("Waiting for wake word 'Jarvis'...")
            wake_word = listen_and_recognize()
            
            if wake_word and "jarvis" in wake_word:
                active = True
                speak("Yaa")
            elif wake_word is None:
                print("Could not understand the wake word. Please try again.")
            continue
        
        # Jarvis is now active and listening for commands
        command = listen_and_recognize()
        
        if command:
            print(f"You said: {command}")
            
            if "open youtue" in command:
                speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")
            elif "open google" in command:
                speak("Opening Google...")
                webbrowser.open("https://www.google.com")
            elif "open stack overflow" in command:
                speak("Opening Stack Overflow...")
                webbrowser.open("https://www.stackoverflow.com")
            elif "open github" in command:
                speak("Opening GitHub...")
                webbrowser.open("https://www.github.com")
#app open command :-
            

#ADD music command to play music

            elif command.lower().startswith("play music"):
                song = command.lower().split("play music", 1)[1].strip()  # Extract song name after 'play music'
                if song in musiclibrary.music_play:
                    speak(f"Playing {song}...")
                    webbrowser.open(musiclibrary.music_play[song])  # Open the YouTube link for the song
                else:
                    speak("Sorry, I couldn't find that song in the library. Please try again.")
                    
# Extract song name after 'play hindi music'
            elif command.lower().startswith("play hindi music"):
                song = command.lower().split("play hindi music", 1)[1].strip()  
                if song in musiclibrary.hindi_music:
                    speak(f"Playing {song}...")
                    webbrowser.open(musiclibrary.hindi_music[song])  # Open the YouTube link for the song
                else:
                    speak("Sorry, I couldn't find that song in the library. Please try again.")
                    #say bye command to exit the loop
            elif any(exit_phrase in command for exit_phrase in ["goodbye", "bye","ok bye","tata", "exit", "see you"]):
                speak("Goodbye! Have a nice day.")
                break  # Exit the loop if the user says goodbye
        else:
            speak("I didn't catch that. Please say the command again.")
        
        # Reset active state after executing commands
        active = False

