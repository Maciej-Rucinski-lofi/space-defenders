# Current state of game

Milestone 0 complete: project setup, game window, and starfield.
Milestone 1 (player shooting) complete for a single ship.
Milestone 2 (enemy spawning) complete: periodic edge spawn and basic movement.
Milestone 3 (enemy AI) partial: three enemy types with steering variation.
Bullet–enemy collisions complete: circular hitboxes, lethal hits, safe list removal.
Milestone 4 (wave system) complete: finite waves, intermission, wave HUD.

## Implemented

- Python 3.12 + Pygame project structure under `src/`
- Configuration module (`config/settings.py`) with window size, title, and target FPS
- `Game` class managing pygame init, main loop, quit handling, and FPS cap
- Space background with randomly placed star field
- Window closes on quit button or ESC key
- `Player` entity (position, velocity, rotation, rotation speed, thrust force, shoot cooldown)
- Asteroids-style movement: rotate (arrow left/right), thrust (up arrow), inertia, frame-rate independent delta time
- Placeholder triangle ship rendered at correct orientation
- Player spawns at screen center, zero velocity, facing left
- Screen wrapping: ship reappears on the opposite edge when leaving the screen; velocity and rotation are preserved
- Maximum player velocity clamp (500 px/s)
- Automatic shooting: bullets every 300ms at ship position, direction from ship rotation
- `Bullet` entity with position, velocity, direction, and lifespan timer
- `BulletSystem` updates positions, expires bullets after 2.5s, and removes bullets that leave the screen (100px margin)
- `Enemy` entity (position, velocity, rotation, speed, health, type, steering state)
- `EnemySpawner` spawns enemies every 2s from a random screen edge (40px off-screen)
- Three enemy types (Chaser, Drifter, Kamikaze) with distinct speed, steering, and colours
- Enemies steer toward the player with periodic steering offset changes
- F3 debug overlay: target/velocity lines and circular collision hitboxes
- `CollisionSystem`: bullet–enemy circle overlap; one bullet destroys one enemy; deferred removal from lists
- `WaveManager`: wave progression with linear enemy scaling (5, 8, 11, 14, …); gradual spawn via existing interval; 3s intermission between waves
- Wave HUD: current wave number displayed top-left

## Controls (player 1)

- **Left arrow** — rotate left
- **Right arrow** — rotate right
- **Up arrow** — thrust forward (ship keeps moving when released)
- **F3** — toggle enemy AI and collision debug overlay
- **ESC** — quit

## Not yet implemented

- Enemy shooting
- Player damage from enemy bullets or contact
- Second player
- Player health and game over
- Scoring and audio

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
