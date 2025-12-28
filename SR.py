import speech_recognition as sr
import pyttsx3
import time

# ---------------- TTS ENGINE SETUP ----------------

engine = pyttsx3.init()
engine.setProperty("rate", 170)     # speaking speed
engine.setProperty("volume", 1.0)   # volume (0.0 to 1.0)

# ---------------- AI SPEAK ----------------

def ai_speak(text):
    """
    Converts text to speech using offline Windows-safe TTS.
    """
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

# ---------------- AI LISTEN ----------------

def ai_listen():
    """
    Listens through the microphone and converts speech to text.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("(You can speak now)")
            audio_data = recognizer.listen(source)

        user_input = recognizer.recognize_google(audio_data)
        print(f"You said: {user_input}")
        return user_input.lower()

    except sr.UnknownValueError:
        print("AI: I could not understand your speech.")
        return ""

    except sr.RequestError as e:
        print(f"AI: Speech recognition service error: {e}")
        return ""

    except Exception as e:
        print(f"AI: Unexpected error: {e}")
        return ""

# ---------------- MAIN LOOP ----------------

def run_ai_interaction():
    ai_speak("Greetings! I am your personal AI assistant, ready to assist you.")
    time.sleep(1)

    while True:
        ai_speak("What would you like to do? Say Text to Speech, Speech to Text, or Exit.")
        user_choice = ai_listen()

        if "text to speech" in user_choice or "tts" in user_choice:
            ai_speak("Please type the sentence you want me to speak.")
            text = input("You (type): ").strip()

            if text:
                ai_speak(text)
            else:
                ai_speak("No text was provided.")

        elif "speech to text" in user_choice or "stt" in user_choice:
            ai_speak("Please speak clearly.")
            result = ai_listen()

            if result:
                ai_speak(f"I believe you said: {result}")
            else:
                ai_speak("I could not capture any speech.")

        elif "exit" in user_choice or "quit" in user_choice or "goodbye" in user_choice:
            ai_speak("Farewell. Goodbye.")
            break

        else:
            ai_speak("I did not understand your request. Please try again.")

        time.sleep(1.5)

# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    run_ai_interaction()
