# Current state of game

Milestone 0 complete: project setup, game window, and starfield.
Milestone 1 (player shooting) complete for both ships.
Milestone 2 (enemy spawning) complete: periodic edge spawn and basic movement.
Milestone 3 (enemy AI) partial: three enemy types with steering variation.
Bullet–enemy collisions complete: circular hitboxes, lethal hits, safe list removal.
Milestone 4 (wave system) complete: finite waves, intermission, wave HUD.
Milestone 5 (player health and game over) complete: HP, collision damage, destruction, game-over state.
Local co-op complete: two players on one keyboard with independent controls, health, and shooting.
Level system architecture complete: `Game` owns a `LevelManager`; survival gameplay lives in `SurvivalLevel`; `FormationLevel` is a placeholder.

## Implemented

- Python 3.12 + Pygame project structure under `src/`
- Configuration module (`config/settings.py`) with window size, title, and target FPS
- `Game` class managing pygame init, main loop, quit handling, FPS cap, and level delegation
- Level layer: `BaseLevel` lifecycle, `LevelManager` (one active level), `SurvivalLevel` (existing gameplay), `FormationLevel` (placeholder)
- Space background with randomly placed star field
- Window closes on quit button or ESC key
- `Player` entity (position, velocity, rotation, rotation speed, thrust force, shoot cooldown, health, max health, destroyed flag)
- Asteroids-style movement: rotate, thrust, inertia, frame-rate independent delta time
- Placeholder triangle ship rendered at correct orientation
- Two players spawn left and right of screen center (`SPAWN_HORIZONTAL_OFFSET` in `config/player.py`)
- Screen wrapping: ship reappears on the opposite edge when leaving the screen; velocity and rotation are preserved
- Maximum player velocity clamp (500 px/s)
- Automatic shooting: bullets every 300ms at ship position, direction from ship rotation; independent cooldown per player
- `Bullet` entity with position, velocity, direction, and lifespan timer
- `BulletSystem` updates positions, expires bullets after 2.5s, and removes bullets that leave the screen (100px margin)
- `Enemy` entity (position, velocity, rotation, speed, health, type, steering state)
- `EnemySpawner` spawns enemies every 2s from a random screen edge (40px off-screen)
- Three enemy types (Chaser, Drifter, Kamikaze) with distinct speed, steering, and colours
- Enemies steer toward the nearest living player with periodic steering offset changes
- F3 debug overlay: per-enemy target/velocity lines and circular collision hitboxes
- `CollisionSystem`: bullet–enemy and enemy–player circle overlap; deferred removal from lists
- `WaveManager`: wave progression with linear enemy scaling; gradual spawn via existing interval; 3s intermission between waves
- Wave HUD: current wave number and remaining enemies displayed top-left
- Player health: 100 HP max, 25 damage per enemy collision, text HUD (`P1 HP: …`, `P2 HP: …`)
- Enemy–player collisions: suicidal enemy attack removes enemy and damages the hit player only
- Destroyed players cannot move, shoot, or render
- `GameState`: RUNNING / GAME_OVER; co-op continues while any player lives
- Game over screen: centered **GAME OVER** and wave reached; gameplay updates stop

## Controls

### Player 1

- **W** — thrust forward
- **A** — rotate left
- **D** — rotate right

### Player 2

- **Up arrow** — thrust forward
- **Left arrow** — rotate left
- **Right arrow** — rotate right

### Global

- **F3** — toggle enemy AI and collision debug overlay (SurvivalLevel)
- **F5** — switch to FormationLevel (placeholder)
- **F6** — switch back to SurvivalLevel
- **ESC** — quit

## Not yet implemented

- Formation Mode gameplay (formations, bombs, multi-hit enemies)
- Enemy shooting
- Restart after game over
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
