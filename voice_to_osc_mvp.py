"""
Voice-controlled OSC interface for Ableton Live.

This script listens to microphone input, parses voice commands using a predefined
dictionary (loaded from JSON), and sends corresponding OSC messages to Ableton Live.
"""

import json
import speech_recognition as sr
from pythonosc.udp_client import SimpleUDPClient


# Constants
OSC_IP = "127.0.0.1"
OSC_PORT = 11000
COMMANDS_FILE = "commands.json"

# Load commands from JSON file
with open(COMMANDS_FILE, "r") as file:
    COMMANDS = json.load(file)

# Initialize OSC client
client = SimpleUDPClient(OSC_IP, OSC_PORT)


def normalize(text: str) -> str:
    """
    Normalize user input for better command matching.

    Args:
        text (str): Raw text from voice recognition.

    Returns:
        str: Cleaned and normalized text.
    """
    return text.lower().strip().replace("new", "")


def parse_command(text: str):
    """
    Match user text to a known OSC command from the loaded JSON.

    Args:
        text (str): Normalized voice input.

    Returns:
        tuple: (osc_path, arguments, response_message) if match found, else (None, None, None)
    """
    text = normalize(text)
    for phrase, details in COMMANDS.items():
        if phrase in text:
            path = details["path"]
            args = details["args"]
            response = details["response"]
            print(f"✅ Matched: '{phrase}' → {path} {args}")
            return path, args, response

    print("❓ No matching command found.")
    return None, None, None


def listen_and_trigger():
    """
    Listen to microphone input, transcribe speech, match it to a command,
    and send the corresponding OSC message to Ableton.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎧 Listening... say something!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣 You said: {text}")

        path, args, response = parse_command(text)
        if path:
            client.send_message(path, args)
            print(f"🎛️ Sent: {path} {args}")
            print(f"🗣️  {response}")

    except sr.UnknownValueError:
        print("🙉 Sorry, didn’t catch that.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results from Google Speech Recognition service: {e}")


def main():
    """
    Main event loop: continuously listens and processes voice commands.
    """
    while True:
        listen_and_trigger()


if __name__ == "__main__":
    main()
