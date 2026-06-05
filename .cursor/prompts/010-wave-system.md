# 010-wave-system

## Goal

Implement a wave-based progression system.
Enemies should spawn in organized waves rather than continuously forever.
The game should clearly progress from one wave to the next.
This milestone introduces game progression but does not yet introduce scoring, player health, or game over conditions.

---

## Context

The game currently includes:

* player movement
* automatic shooting
* bullet system
* enemy spawning
* enemy movement
* enemy destruction through collisions

At the moment enemies spawn continuously.
The game now needs a progression system that creates short moments of action followed by brief pauses before the next challenge.

---

## Requirements

## Wave Manager

Create a dedicated Wave Manager responsible for:

* current wave number
* enemies remaining to spawn
* active enemies
* wave transitions

Avoid embedding wave logic directly inside enemy spawning code.

---

## Wave Structure

Each wave has:

* wave number
* total enemies to spawn

Suggested formula:

```text
Wave 1 -> 5 enemies
Wave 2 -> 8 enemies
Wave 3 -> 11 enemies
Wave 4 -> 14 enemies
```

Simple linear scaling is sufficient.

---

## Enemy Spawning During Wave

Enemies should not all appear at once.

Instead:
* spawn enemies gradually
* reuse existing spawn interval logic

Example:

```text
Wave 1:
Spawn 5 enemies
1 enemy every 1.5 seconds
```

---

## Wave Completion

A wave is complete when:

* all wave enemies have been spawned
  AND
* all spawned enemies have been destroyed

Both conditions must be true.

---

## Intermission

After completing a wave:

Pause briefly before starting the next wave.

Recommended:

```text
INTERMISSION_DURATION = 3 seconds
```

During intermission:

* no enemies spawn
* players can continue moving

---

## Wave Counter

Display current wave number on screen.

Minimal UI is sufficient.

Example:

```text
Wave 3
```

Display location:

* top-left corner
  OR
* top-center

Keep styling simple.

---

## Next Wave Start

When intermission ends:

* increment wave number
* initialize next wave
* begin spawning enemies

Progression should continue indefinitely.

---

## Architecture Notes

Introduce a dedicated system or manager:

Examples:

* WaveManager
* WaveSystem

Responsibilities:

* wave progression
* enemy count tracking
* intermission timing

Do not merge wave logic into:

* rendering
* collision system
* player logic

---

## Out of Scope

Do NOT implement:

* scoring
* player health
* game over
* victory screen
* bosses
* difficulty modifiers
* power-ups
* save system

---

## Acceptance Criteria

* Game starts at Wave 1
* Wave contains a finite number of enemies
* Enemies spawn gradually
* Wave ends when all enemies are destroyed
* Intermission occurs between waves
* Next wave starts automatically
* Wave number increases correctly
* Current wave number is visible on screen
* Progression can continue indefinitely

---

## Manual Test Plan

### Test 1

Start game.

Expected:

* Wave 1 begins.

### Test 2

Destroy all enemies.

Expected:

* Wave completes.

### Test 3

Wait during intermission.

Expected:

* No enemies spawn.

### Test 4

Intermission ends.

Expected:

* Wave 2 begins automatically.

### Test 5

Reach Wave 3+.

Expected:

* Enemy count increases correctly.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed work to tasks/completed.md.
3. Add the next milestone to tasks/current.md.
