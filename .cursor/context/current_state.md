# Current state of game

Milestone 0 complete: project setup and game window.

## Implemented

- Python 3.12 + Pygame project structure under `src/`
- Configuration module (`config/settings.py`) with window size, title, and target FPS
- `Game` class managing pygame init, main loop, quit handling, and FPS cap
- Space background with randomly placed star field
- Window closes on quit button or ESC key

## Not yet implemented

- Player ships and movement
- Shooting
- Enemies, AI, waves
- Collisions and HP
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
