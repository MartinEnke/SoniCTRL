# 🎙️ SoniCTRL — Voice-Controlled OSC Assistant for Ableton Live

SoniCTRL is a voice-controlled interface that lets you speak to Ableton Live using natural commands.  
It captures your voice, maps it to commands defined in a JSON file, and sends OSC messages to Ableton using [AbletonOSC](https://github.com/ideoforms/AbletonOSC).

No buttons. No clicks. Just your voice and your music. 🎛️✨

---

## ✅ Features

- 🎤 Hands-free control of Ableton Live
- 🧠 Natural command parsing
- 🎚️ OSC message handling with [python-osc](https://pypi.org/project/python-osc/)
- 🗂️ Modular command loading via `commands.json`
- 🧼 Clean and extendable Python codebase

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install speechrecognition python-osc
```

(If you want to test voice output later, you can also install `pyttsx3`.)

---

### 2. Setup AbletonOSC

Follow the [AbletonOSC setup guide](https://github.com/ideoforms/AbletonOSC) to:

- Download and run `run-console.py`
- Ensure Ableton is open
- Make sure AbletonOSC is running and listening on port `11000`

---

### 3. Create Your Command Dictionary

All voice commands and their corresponding OSC paths live in:

```bash
commands.json
```

Example:

```json
{
  "start playing": {
    "path": "/live/song/start_playing",
    "args": [],
    "response": "Starting playback."
  }
}
```

---

### 4. Run the Assistant

```bash
python voice_to_osc.py
```

Then just say something like:

> “Create MIDI track”  
> “Stop playing”  
> “Tap tempo”

---

## 📂 Project Structure

```
voice_to_osc.py       # Main voice interface
commands.json         # Configurable command dictionary
README.md             # You are here :)
```

---

## 📦 Future Ideas

## 📦 Future Ideas

- **Fuzzy matching** for flexible phrasing (`"start playback"` = `"start playing"`)
- **AI-enhanced parsing** with GPT (e.g., `"load a synth and record"` → multi-step command)
- **GUI or browser-based dashboard** to visualize commands, logs, and mic input
- **Bundle into a native app** with a tray icon, auto-start, and a "Push-to-Talk" toggle

- **"Always listening" mode** with wake word detection (`"Hey Soni"`)
- **Multi-language support** (`"Spiele ab"`, `"Commencer la lecture"`)
- **Plugin-specific commands** like `"load Glue Compressor on track 1"`
- **Command chaining** — “create MIDI track and record on it”
- **Voice macro recording** — record a sequence of actions by voice, name it, and replay
- **Text-to-voice confirmation option** (e.g., “Clip launched on track 2”)
- **MIDI fallback/dual control** — use MIDI input and voice interchangeably
- **Session logging** — auto-log what actions were triggered during a session
- **Voice-based authentication** or confirmation for critical actions
- ☁**Cloud sync of command sets** across machines
- **Test mode** — dry-run without sending OSC, just to test command recognition
- **Clip-specific controls** — “duplicate clip in slot 2 of track 4”
- **Profile switching** — DJ mode, live mode, studio mode, etc.





🎛️ GUI or browser-based dashboard to visualize commands, logs, and mic input

📦 Bundle into a native app with a tray icon, auto-start, and a "Push-to-Talk" toggle

🎧 "Always listening" mode with wake word detection ("Hey Soni")

🗣️ Multi-language support ("Spiele ab", "Commencer la lecture")

🧩 Plugin-specific commands like "load Glue Compressor on track 1"

🧵 Command chaining — “create MIDI track and record on it”

📋 Voice macro recording — record a sequence of actions by voice, name it, and replay

🎙 Text-to-voice confirmation option (e.g., “Clip launched on track 2”)

🕹 MIDI fallback/dual control — use MIDI input and voice interchangeably

📊 Session logging — auto-log what actions were triggered during a session

🔐 Voice-based authentication or confirmation for critical actions

☁️ Cloud sync of command sets across machines

🧪 Test mode — dry-run without sending OSC, just to test command recognition

🎤 Clip-specific controls — “duplicate clip in slot 2 of track 4”

🗂️ Profile switching — DJ mode, live mode, studio mode, etc.

---

## 💬 Credits

Built by me and assisted by ChatGPT 🚀  
Powered by [AbletonOSC](https://github.com/ideoforms/AbletonOSC)

---

## 🧪 MVP Status

This is an early version of SoniCTRL designed for rapid iteration and experimentation.  
Feedback, ideas, and contributions are welcome!
