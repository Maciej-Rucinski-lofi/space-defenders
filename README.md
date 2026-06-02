# Space Defenders

A cooperative 2D space shooter built with Python and Pygame. Two players pilot small spacecraft, fight waves of enemies, and survive together.

## About the game

- **Co-op:** two players on one screen
- **Movement:** ships rotate in place and accelerate forward (no friction)
- **Combat:** automatic firing for players and enemies
- **Waves:** enemies spawn from the screen edges; a wave ends when all enemies are destroyed

## Current status

**Milestone 0** is complete: project setup, game window, and animated starfield background.

Not yet implemented: player ships, shooting, enemies, AI, waves, collisions, HUD, and audio.

## Tech stack

- Python 3.12
- [Pygame](https://www.pygame.org/) 2.5+
- ECS-inspired layout: entities hold state, systems hold behaviour, `Game` orchestrates the loop

## Requirements

- Python 3.12
- pip

## Getting started

### Setup

**Windows (PowerShell):**

```powershell
.\scripts\setup.ps1
```

**Linux / macOS:**

```bash
chmod +x scripts/setup.sh scripts/run.sh
./scripts/setup.sh
```

**Manual setup:**

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

### Run

**Windows (PowerShell):**

```powershell
.\scripts\run.ps1
```

**Linux / macOS:**

```bash
./scripts/run.sh
```

**Manual run** (with the virtual environment activated):

```bash
cd src
python main.py
```

Close the game with the window close button or **ESC**.

## Project structure

```
space-defenders/
├── src/
│   ├── main.py           # Entry point
│   ├── config/           # Window size, title, FPS
│   ├── game/             # Game loop and rendering
│   ├── entities/         # Player, enemy, bullet data (planned)
│   └── systems/          # Gameplay systems (planned)
├── scripts/              # setup and run helpers
├── requirements.txt
└── .cursor/              # Project rules and task tracking
```

## Roadmap

| Milestone | Focus |
|-----------|--------|
| 0 | Space map |
| 1 | Shooting |
| 2 | Enemy spawning |
| 3 | Enemy AI |
| 4 | Wave system |
| 5 | Game over |

## Repository

https://github.com/Maciej-Rucinski-lofi/space-defenders
