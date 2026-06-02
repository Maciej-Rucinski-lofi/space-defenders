# 007-enemy-spawning

## Goal

Implement enemy spawning system for the game.
Enemies should appear from the edges of the screen and move into the play area.
This milestone focuses only on spawning and basic enemy movement.
Do not implement collision damage, scoring, or advanced enemy AI or second player yet.

---

## Context

The game already includes:

* player movement with inertia
* screen wrapping
* automatic shooting
* bullet system with lifecycle management

Now the game needs external threats to create gameplay pressure.
Enemies are the first step toward actual gameplay loop.

---

## Requirements

### Enemy Entity

Create an Enemy entity with:

* position
* velocity
* rotation (optional)
* speed
* health (simple value, e.g. 1–3)

Enemies should be simple at this stage.

---

## Spawning System

Implement an enemy spawning system.

### Spawn Locations

Enemies must spawn randomly from one of the screen edges:
* top
* bottom
* left
* right

Spawn position should be slightly outside the screen bounds (off-screen spawn).

---

### Spawn Direction

Enemies should move inward toward the play area.

Basic behaviour:
* calculate direction toward center of screen OR nearest player
* set velocity toward that direction

---

### Spawn Timing

Enemies should spawn periodically:

* `ENEMY_SPAWN_INTERVAL_MS = 1500–3000` (tunable)

Spawn interval can be constant at first.

---

### Difficulty Baseline

Initial enemy stats:

* slow movement speed
* low health
* no shooting (yet optional but recommended to skip for now)

---

## Movement

Enemies must:

* move continuously
* not require player interaction to update
* respect delta time for movement

---

## Optional Simple Behaviour

If implemented, enemies may:
* slightly adjust direction toward nearest player over time

But full AI is not required in this milestone.

---

## Architecture Notes

* Enemy spawning should be handled in a dedicated system (e.g. `EnemySpawner`)
* Enemy update logic should be separate from rendering
* Enemies should be stored in central game entity collection
* Avoid coupling enemy logic with player or bullet systems

---

## Out of Scope

Do NOT implement:

* collision detection
* damage system
* scoring
* enemy shooting
* advanced AI
* wave system
* boss enemies
* power-ups

---

## Acceptance Criteria

* Enemies spawn periodically
* Enemies spawn from screen edges (random side)
* Enemies move toward play area
* Enemies are visible and updated every frame
* Enemy count increases over time
* No collision or combat logic is implemented yet
