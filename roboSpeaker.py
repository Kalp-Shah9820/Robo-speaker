import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker! created by Kalp Shah")
    while True:
        x=input("Enter what u want me to say: ")
        if x=="q":
            engine.say("'Goodbye'")
            engine.runAndWait()
            break
        engine.setProperty('rate', 150)  

        engine.say(x)
        engine.runAndWait()
        

