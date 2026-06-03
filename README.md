# Space Defenders

A cooperative 2D space shooter built with Python and Pygame. Two players pilot small spacecraft, fight waves of enemies, and survive together.

## About the game

- **Co-op:** two players on one screen
- **Movement:** ships rotate in place and accelerate forward (no friction)
- **Combat:** automatic firing for players and enemies
- **Waves:** enemies spawn from the screen edges; a wave ends when all enemies are destroyed

## Current status

**Milestone 0** is complete: project setup, game window, and animated starfield background.

**Player movement** is playable for one ship: Asteroids-style rotation and thrust with inertia (no friction), capped at a maximum speed so thrust cannot accelerate forever. Use the **arrow keys** to rotate and thrust forward. The ship wraps to the opposite screen edge when it leaves the visible area.

**Player shooting** (Milestone 1): the ship fires bullets automatically every 300ms in the direction it is facing. Bullets move independently and are removed when their lifetime ends or they leave the screen (with a configurable margin). No collisions or damage yet.

**Enemy spawning** (Milestone 2): enemies spawn every 2 seconds from a random screen edge, slightly off-screen.

**Enemy behaviour** (Milestone 3, partial): three placeholder types spawn at random — **Chaser** (red, direct pursuit), **Drifter** (orange, slower with wider steering jitter), and **Kamikaze** (yellow, faster, unstable path, no shooting when that is added). Movement uses a steering offset that is recomputed every 0.5–2 seconds so paths are not perfectly straight. Press **F3** in-game to toggle debug lines (green = steered target direction, blue = velocity) and circular hitbox outlines for bullets and enemies. Set `ENEMY_AI_SEED` in `config/enemy_behaviour.py` for reproducible AI randomness. No enemy shooting yet.

**Collisions:** player bullets use circular hit detection (`BULLET_RADIUS` in `config/bullet.py`, `ENEMY_RADIUS` in `config/enemy.py`). A hit removes both the bullet and the enemy (one bullet, one enemy). No player damage, scoring, or effects yet.

Not yet implemented: enemy shooting, waves, second player, HUD, and audio.

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

### Controls (player 1)

| Key | Action |
|-----|--------|
| Left arrow | Rotate left |
| Right arrow | Rotate right |
| Up arrow | Thrust forward |
| ESC | Quit |
| F3 | Toggle enemy AI and collision hitbox debug overlay |

## Project structure

```
space-defenders/
├── src/
│   ├── main.py           # Entry point
│   ├── config/           # Game constants (window, player, bullets, enemies, starfield)
│   ├── game/             # Game loop and rendering
│   ├── entities/         # Player, enemy, bullet data
│   ├── systems/          # Input, movement, rendering systems
│   └── world/            # World utilities (e.g. screen wrapping)
├── scripts/              # setup and run helpers
├── requirements.txt
└── .cursor/              # Project rules and task tracking
```

## Roadmap

| Milestone | Focus |
|-----------|--------|
| 0 | Space map |
| 1 | Shooting (player auto-fire) |
| 2 | Enemy spawning |
| 3 | Enemy AI |
| 4 | Wave system |
| 5 | Game over |

## Repository

https://github.com/Maciej-Rucinski-lofi/space-defenders
