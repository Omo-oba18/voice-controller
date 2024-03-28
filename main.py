# main.py
import speech_recognition as sr
from actions import spotify

def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    while True:
        # Capture audio input
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Recognize speech
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            # Perform action based on command
            if "spotify" in command:
                if "play" in command:
                    spotify.play()
                elif "pause" in command:
                    spotify.pause()
                elif "resume" in command:
                    spotify.resume()
                else:
                    print("Sorry, I couldn't understand the action.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("There was an error processing your request.")

if __name__ == "__main__":
    main()
