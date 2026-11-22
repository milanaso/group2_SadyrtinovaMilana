# Practice 7 — Pygame

Three small Pygame projects:

1. `mickeys_clock` — a clock with a Mickey-shaped face and rotating hands.
2. `music_player` — a keyboard-controlled music player.
3. `moving_ball` — a red ball controlled with the arrow keys.

## Install

```bash
python3 -m pip install -r requirements.txt
```

## Run

Run each project from the repository root:

```bash
python3 mickeys_clock/main.py
python3 music_player/main.py
python3 moving_ball/main.py
```

For the music player, put your own `.mp3`, `.wav`, or `.ogg` files in
`music_player/music/`. The player starts with an empty playlist if the folder
contains no supported audio files.

## Controls

### Music player
- `P` — play / pause
- `S` — stop
- `N` — next track
- `B` — previous track
- `Q` or `Esc` — quit

### Moving ball
- Arrow keys — move 20 pixels
- `Q` or `Esc` — quit
