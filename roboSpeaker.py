import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker! created by Kalp Shah")
    while True:
        engine.setProperty('rate', 150)  # Speed (default ~200)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Use female voice (optional)
        x=input("Enter what u want me to say: ")
        if x=="q":
            engine.say("'Goodbye'")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()
        

