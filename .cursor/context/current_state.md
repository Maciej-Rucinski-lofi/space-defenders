# Current state of game

Milestone 0 complete: project setup, game window, and starfield.
Player movement (single ship) is implemented as a continuation of Milestone 0 setup.

## Implemented

- Python 3.12 + Pygame project structure under `src/`
- Configuration module (`config/settings.py`) with window size, title, and target FPS
- `Game` class managing pygame init, main loop, quit handling, and FPS cap
- Space background with randomly placed star field
- Window closes on quit button or ESC key
- `Player` entity (position, velocity, rotation, rotation speed, thrust force)
- Asteroids-style movement: rotate (arrow left/right), thrust (up arrow), inertia, frame-rate independent delta time
- Placeholder triangle ship rendered at correct orientation
- Player spawns at screen center, zero velocity, facing left

## Controls (player 1)

- **Left arrow** — rotate left
- **Right arrow** — rotate right
- **Up arrow** — thrust forward (ship keeps moving when released)

## Not yet implemented

- Shooting
- Enemies, AI, waves
- Collisions and HP
- Second player
- Screen wrapping
- HUD and audio

## Run

### First-time setup (virtual environment)

Windows (PowerShell):

```powershell
.\scripts\setup.ps1
```

Linux / macOS:

```bash
chmod +x scripts/setup.sh scripts/run.sh
./scripts/setup.sh
```

Manual setup:

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

### Start the game

Windows (PowerShell):

```powershell
.\scripts\run.ps1
```

Linux / macOS:

```bash
./scripts/run.sh
```

Manual run (with venv activated):

```bash
cd src
python main.py
```
