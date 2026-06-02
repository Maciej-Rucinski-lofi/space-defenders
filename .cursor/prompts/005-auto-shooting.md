# 005-auto-shooting

## Goal

Implement automatic shooting for the player ship.
The ship should fire bullets automatically at a fixed interval while the game is running.
This milestone focuses only on shooting mechanics for the player.
Do not implement enemies, collision damage or second player yet.

---

## Context

The player ship already supports:
* movement with inertia
* rotation
* screen wrapping
* velocity clamping

Now the ship must be able to emit projectiles continuously.
Shooting should feel consistent and deterministic.

---

## Requirements

### Auto Shooting

Each player ship must automatically fire bullets at a fixed interval:
* `SHOOT_COOLDOWN_MS = 300`

Each time the cooldown expires:
* spawn a bullet at the ship position
* bullet direction = ship forward direction (based on rotation)

---

### Bullet Properties

Each bullet must have:
* position (copy of ship position at spawn)
* velocity (based on ship forward vector)
* speed constant (e.g. 400–600 units/sec)
* lifespan (optional but recommended, e.g. 2–3 seconds)

Bullets move independently after being created.

---

### Direction Calculation

Bullet velocity must be derived from ship rotation:
* forward vector = direction ship is facing
* velocity = forward_vector * bullet_speed

Rotation must directly influence firing direction.

---

### Timing System

Shooting must be time-based, not frame-based:
* use delta time or timestamps
* ensure consistent firing rate regardless of FPS

Each player ship maintains its own cooldown timer.

---

### Multiple Players (Important)

If multiple players exist:
* each player shoots independently
* each player has separate cooldown state
* no shared shooting timer

---

## Architecture Notes

* Shooting logic should not be inside input handling
* Prefer a `ShootingSystem` or `WeaponComponent`
* Bullets should be stored in a central game entity list
* Avoid embedding bullet logic inside Player class if possible

---

## Out of Scope

Do NOT implement:

* collision detection
* enemy interaction
* damage system
* scoring
* sound effects
* bullet-enemy logic
* power-ups

---

## Acceptance Criteria

* Player ship fires bullets automatically every 300ms
* Bullets spawn at ship position
* Bullets travel in direction of ship rotation
* Each player shoots independently (if multiplayer exists)
* Shooting is consistent across FPS variations
* Bullets exist and move independently after spawn
* No collision or damage logic is implemented yet
