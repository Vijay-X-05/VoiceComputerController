import speech_recognition as sr
import subprocess
import os


# Create speech recognizer
recognizer = sr.Recognizer()


print("================================")
print("   VOICE COMPUTER CONTROLLER")
print("================================")
print("Voice controller started.")
print("Say 'stop listening' to stop.\n")


# Keep listening until the user stops the program
while True:

    try:

        # Access microphone
        with sr.Microphone() as source:

            print("Listening...")

            # Reduce effect of background noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            # Listen to user
            audio = recognizer.listen(source)


        # Convert speech into text
        command = recognizer.recognize_google(audio)

        # Convert text to lowercase
        command = command.lower()

        print("You said:", command)


        # -------------------------
        # STOP COMMAND
        # -------------------------

        if "stop listening" in command:

            print("Voice controller stopped.")

            break


        # -------------------------
        # OPEN NOTEPAD
        # -------------------------

        elif "open notepad" in command:

            print("Opening Notepad...")

            subprocess.Popen(["notepad.exe"])


        # -------------------------
        # OPEN CALCULATOR
        # -------------------------

        elif "open calculator" in command:

            print("Opening Calculator...")

            subprocess.Popen(["calc.exe"])


        # -------------------------
        # OPEN CHROME
        # -------------------------

        elif "open chrome" in command:

            print("Opening Chrome...")

            os.startfile(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )


        # -------------------------
        # UNKNOWN COMMAND
        # -------------------------

        else:

            print("Command not recognized.")


        print()


    # Speech was heard but couldn't be understood
    except sr.UnknownValueError:

        print("Sorry, I could not understand you.\n")


    # Problem communicating with speech recognition service
    except sr.RequestError as error:

        print("Speech recognition error:", error)
        print()


    # Other unexpected errors
    except Exception as error:

        print("Error:", error)
        print()