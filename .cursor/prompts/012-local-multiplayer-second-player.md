# 012-local-multiplayer-second-player

## Goal

Add a second local player controlled from the same keyboard.
The game should support two simultaneous players cooperating against enemy waves.
This milestone focuses on introducing Player 2 while preserving all existing gameplay systems.

---

## Context

The game currently supports:

* a single player ship
* movement with inertia
* automatic shooting
* enemy spawning
* enemy destruction
* wave progression
* player health and game over

The game concept is cooperative local multiplayer.
Player systems should now be generalized to support multiple players.

---

## Requirements

## Player 2 Entity

Create a second player ship.

Player 2 should have the same capabilities as Player 1:

* movement
* rotation
* thrust
* automatic shooting
* health
* screen wrapping
* collision participation

Both players should use the same Player entity type.

Avoid creating a separate PlayerTwo class.

---

## Spawn Positions

Players should start in different locations.

Example:

```text
Player 1 -> left side of center
Player 2 -> right side of center
```

Players should not overlap at spawn.

---

## Controls

### Player 1

* W = thrust
* A = rotate left
* D = rotate right

### Player 2

* Up Arrow = thrust
* Left Arrow = rotate left
* Right Arrow = rotate right

Controls must work simultaneously.

Holding keys for one player must not interfere with the other.

---

## Shooting

Player 2 should automatically fire using the same rules as Player 1.

Requirements:

* independent cooldown
* independent bullet spawning
* independent position and direction

Both players should be able to shoot simultaneously.

---

## Health System

Each player must maintain separate:

* health
* destruction state

Damage to one player must not affect the other.

---

## Enemy Targeting

Update enemy targeting logic.

Enemies should:

* target the nearest living player

If one player is destroyed:

* enemies should target the remaining player

---

## Multiplayer Game Flow

The game continues while at least one player is alive.

Game Over occurs only when:

* Player 1 is destroyed
  AND
* Player 2 is destroyed

---

## Architecture Notes

Refactor any existing single-player assumptions.

Examples of anti-patterns:

```python
game.player
```

Prefer:

```python
game.players
```

Systems should operate on collections of players rather than a single player instance.

Avoid duplicating gameplay logic.

---

## User Interface

Display health for both players.

Example:

```text
P1 HP: 100
P2 HP: 100
```

Simple text rendering is sufficient.

---

## Out of Scope

Do NOT implement:

* player-to-player collisions
* friendly fire
* player revival
* shared health
* split screen
* controller support
* network multiplayer

---

## Acceptance Criteria

* Two players are visible
* Both players can move independently
* Both players can rotate independently
* Both players automatically shoot
* Both players can be damaged independently
* Enemy AI targets nearest living player
* Health is displayed for both players
* Game continues if one player dies
* Game Over occurs only when both players are destroyed
* No duplicated gameplay code is introduced

---

## Manual Test Plan

### Test 1

Move both players simultaneously.

Expected:

* Both respond correctly.

### Test 2

Observe automatic shooting.

Expected:

* Both players fire independently.

### Test 3

Destroy Player 1.

Expected:

* Player 2 remains playable.

### Test 4

Observe enemy behaviour.

Expected:

* Enemies target nearest living player.

### Test 5

Destroy both players.

Expected:

* Game Over appears.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed work to tasks/completed.md.
3. Add the next milestone to tasks/current.md.

Do not modify architecture documents.
