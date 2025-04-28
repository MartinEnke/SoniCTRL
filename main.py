from osc_listener import OSCListener  # import your new listener class
from pythonosc.udp_client import SimpleUDPClient
import speech_recognition as sr
import json

client = SimpleUDPClient("127.0.0.1", 11000)
listener = OSCListener()  # initialize only once

# Load commands
with open("commands.json", "r") as f:
    COMMANDS = json.load(f)

def normalize(text):
    return text.lower().strip()

def parse_command(text):
    text = normalize(text)
    for phrase, data in COMMANDS.items():
        if phrase in text:
            return data["path"], data["args"], data["response"]
    return None, None, None

def listen_and_trigger():
    """
    Listens for a voice command, parses it, and sends the appropriate OSC message(s).
    Supports multiple commands with dynamic placeholders like 'SELECTED'.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening... say something!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣 You said: {text}")

        path, args, response = parse_command(text)
        if not path:
            print("❓ No command matched.")
            return

        # Handle multiple commands
        if isinstance(path, list):
            for p, a in zip(path, args):
                if isinstance(a, list) and "SELECTED" in a:
                    listener.watch("/live/view/selected_track")
                    client.send_message("/live/view/get/selected_track", [])
                    track_index = listener.get("/live/view/selected_track")
                    if track_index is None:
                        print("⚠️ Could not retrieve selected track index. Defaulting to track 0.")
                        track_index = 0
                    a = [track_index if x == "SELECTED" else x for x in a]

                client.send_message(p, a)
                print(f"🎛️ Sent: {p} {a}")
        else:
            # Single command
            if isinstance(args, list) and "SELECTED" in args:
                listener.watch("/live/view/selected_track")
                client.send_message("/live/view/get/selected_track", [])
                track_index = listener.get("/live/view/selected_track")
                if track_index is None:
                    print("⚠️ Could not retrieve selected track index.")
                    return
                args = [track_index if arg == "SELECTED" else arg for arg in args]

            client.send_message(path, args)
            print(f"🎛️ Sent: {path} {args}")

        print(f"🗣️ {response}")

    except sr.UnknownValueError:
        print("🙉 Sorry, didn’t catch that.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results: {e}")


if __name__ == "__main__":
    while True:
        listen_and_trigger()
