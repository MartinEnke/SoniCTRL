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

This tool lets you control Ableton Live with your voice using OSC commands.  
Speak commands like **“start playing”** or **“create midi and record”** — and Ableton responds.

---

## 📦 1. Installation

### Step-by-step setup:

1. **Clone the repository and navigate into it:**

```bash
git clone git@github.com:MartinEnke/SoniCTRL.git
cd SoniCTRL
```

2. **(Optional) Create a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

3. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

> Or manually (if needed):

```bash
pip install speechrecognition python-osc pyaudio
```

> ✅ Optional:  
To enable **voice responses**, you can also install:

```bash
pip install pyttsx3
```

4. **Run the assistant:**

```bash
python voice_to_osc_mvp.py
```

---

## 🎛️ 2. Setup AbletonOSC

This tool communicates with Ableton Live via [AbletonOSC](https://github.com/ideoforms/AbletonOSC).

Make sure you:

- Download and install AbletonOSC per their guide
- Copy the `AbletonOSC` folder into your Ableton `Remote Scripts` directory:
  - macOS: `~/Music/Ableton/User Library/Remote Scripts/`
- Launch Ableton Live
- In **Preferences > MIDI**, set a Control Surface to `AbletonOSC`
- Run `run-console.py` from the AbletonOSC folder to keep it listening on port `11000`

---

## 🎤 3. Create Your Command Dictionary

All voice commands are defined in the `commands.json` file.

### Example:

```json
{
  "start playing": {
    "path": "/live/song/start_playing",
    "args": [],
    "response": "Starting playback."
  }
}
```

You can add or modify commands anytime to match your workflow.

---

## 🏁 4. Run the Assistant

Once setup is complete:

```bash
python voice_to_osc_mvp.py
```

Say something like:

> 🎙️ “Create audio track”  
> 🎙️ “Stop playing”  
> 🎙️ “Create midi and record”

…and let Ableton follow your voice. 🎧✨


```

Then just say something like:

> “Create MIDI track”  
> “Play”  
> “Tap tempo”

---

## 📂 Project Structure

```
voice_to_osc_mvp.py       # Main voice interface
commands.json         # Configurable command dictionary
README.md             # You are here :)
requirements.txt     
```

---

## Future Ideas

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


---

## 💬 Credits

Built by me and assisted by ChatGPT 🚀  
Powered by [AbletonOSC](https://github.com/ideoforms/AbletonOSC)

---

## 🧪 MVP Status

This is an early version of SoniCTRL designed for rapid iteration and experimentation.  
Feedback, ideas, and contributions are welcome!
