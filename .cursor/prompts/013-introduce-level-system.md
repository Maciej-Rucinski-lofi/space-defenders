# 013-introduce-level-system

## Goal

Introduce a Level System that allows the game to support multiple gameplay modes.

This milestone focuses on architecture only.

Do not implement Formation Mode gameplay yet.

The goal is to create the foundation that will allow different level types to coexist without modifying existing gameplay systems.

---

## Context

The game currently contains a single gameplay experience:

* Asteroids-style movement
* screen wrapping
* wave progression
* enemies spawning from screen edges

A new gameplay mode is planned:

Formation Mode

Features of the future mode:

* players near the bottom of the screen
* enemy formations
* enemy bombs
* multi-hit enemies

These rules differ significantly from the current gameplay.

A Level System is required before implementing the new mode.

---

## Requirements

## Create Level Abstraction

Introduce a common level abstraction.

Examples:

* BaseLevel
* AbstractLevel

The abstraction should define the common lifecycle of a level.

Examples:

* initialize
* update
* render
* cleanup
* completion status

Choose naming that fits the project architecture.

---

## Create LevelManager

Create a LevelManager responsible for:

* owning the active level
* updating the active level
* rendering the active level
* switching between levels

Only one level may be active at a time.

---

## Create SurvivalLevel

Move existing gameplay into a dedicated SurvivalLevel.

Current gameplay must continue working exactly as before.

SurvivalLevel should contain:

* wave progression
* enemy spawning
* survival-specific victory conditions

No gameplay changes are required.

This is a refactor, not a redesign.

---

## Create FormationLevel Placeholder

Create an empty FormationLevel.

The class should exist but contain minimal functionality.

Examples:

* empty update
* empty render
* placeholder completion state

Do not implement formations, bombs, or enemies yet.

The objective is only to validate the architecture.

---

## Level Switching

Implement the ability to switch levels through the LevelManager.

Temporary testing approach is acceptable.

Example:

```text
Start Game
    ↓
SurvivalLevel

Press F5
    ↓
FormationLevel
```

Any simple testing mechanism is acceptable.

Automatic progression is NOT required yet.

---

## Preserve Existing Gameplay

All current gameplay must continue functioning:

* player movement
* shooting
* collisions
* enemy spawning
* waves
* multiplayer

The refactor must not change gameplay behaviour.

---

## Architecture Notes

Responsibilities:

### Game

* application lifecycle
* rendering pipeline
* input collection
* owns LevelManager

### LevelManager

* owns active level
* performs transitions

### Levels

* define gameplay rules
* coordinate systems
* define completion conditions

### Systems

* contain gameplay behaviour

### Entities

* contain state only

---

## Out of Scope

Do NOT implement:

* Formation Mode gameplay
* enemy formations
* enemy bombs
* bosses
* new enemy types
* level transitions after Wave 3
* cutscenes
* loading screens

This milestone is architecture only.

---

## Acceptance Criteria

* Base level abstraction exists
* LevelManager exists
* SurvivalLevel exists
* FormationLevel placeholder exists
* Existing gameplay works inside SurvivalLevel
* LevelManager can switch between levels
* Only one active level exists at a time
* No gameplay regressions are introduced

---

## Manual Test Plan

### Test 1

Start game.

Expected:

* SurvivalLevel loads.

### Test 2

Play the game.

Expected:

* Existing gameplay behaves exactly as before.

### Test 3

Trigger manual level switch.

Expected:

* FormationLevel becomes active.

### Test 4

Switch back to SurvivalLevel.

Expected:

* Gameplay resumes correctly.

---

## Documentation Updates

After implementation:

1. Update architecture documentation if required.
2. Update context/current_state.md.
3. Move completed tasks to tasks/completed.md.
4. Add the next milestone to tasks/current.md.

Do not modify gameplay rules during this milestone.
