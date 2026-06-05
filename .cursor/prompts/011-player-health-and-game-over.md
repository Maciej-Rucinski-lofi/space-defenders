# 011-player-health-and-game-over

## Goal

Implement player health, enemy-player collisions, and a game over state.
This milestone introduces failure conditions and makes survival meaningful.
Players should be able to lose health when enemies collide with them, and the game should end when all players are destroyed.

---

## Context

The game currently includes:

* player movement
* automatic shooting
* bullet system
* enemy spawning
* enemy destruction
* wave progression

Currently there is no way for players to lose.

This milestone introduces risk and creates a complete gameplay loop.

---

## Requirements

## Player Health

Each player must have:

* current health
* maximum health

Recommended values:

```text
MAX_HEALTH = 100
```

Health values should be configurable.

---

## Health Display

Display player health on screen.

Minimum requirement:

```text
P1 HP: 100
```

If multiplayer exists:

```text
P1 HP: 100
P2 HP: 100
```

Simple text rendering is sufficient.

No health bars required.

---

## Enemy-Player Collision

Implement collision detection between:

* Enemy
* Player

Use the same collision approach already used for bullets and enemies.

Recommended:

* circular collision bounds

---

## Collision Damage

When an enemy collides with a player:

### Player

* lose health

Recommended:

```text
ENEMY_COLLISION_DAMAGE = 25
```

### Enemy

* remove enemy from game

Treat enemy collisions as suicidal attacks.

---

## Player Destruction

When player health reaches zero:

* mark player as destroyed
* remove ship from active gameplay

Destroyed players:

* cannot move
* cannot shoot
* cannot interact

---

## Multiplayer Behaviour

If multiple players exist:

### Cooperative Mode

Game continues while at least one player remains alive.

Only trigger Game Over when:

* all players are destroyed

This supports cooperative gameplay.

---

## Game Over State

Introduce a dedicated game state.

Example:

```text
RUNNING
GAME_OVER
```

When Game Over occurs:

* stop wave progression
* stop enemy spawning
* stop gameplay updates

Rendering may continue.

---

## Game Over Screen

Display a simple message:

```text
GAME OVER
```

Also display:

```text
Wave Reached: X
```

Keep presentation simple.

No restart functionality yet.

---

## Architecture Notes

Create clear separation of responsibilities:

### Collision System

Responsible for:

* enemy-player collisions

### Health System (or Player Entity)

Responsible for:

* health updates
* destruction state

### Game State Manager

Responsible for:

* running/game-over state transitions

Avoid placing game-over logic inside collision code.

---

## Out of Scope

Do NOT implement:

* restart functionality
* score system
* player respawning
* invulnerability frames
* power-ups
* boss enemies
* animations
* sound effects

---

## Acceptance Criteria

* Players have health
* Health is displayed on screen
* Enemy-player collisions deal damage
* Enemy is removed after collision
* Players are destroyed at zero HP
* Dead players cannot move or shoot
* Game continues while at least one player survives
* Game Over occurs when all players are destroyed
* Game Over screen displays correctly
* Wave progression stops after Game Over

---

## Manual Test Plan

### Test 1

Collide with enemy.

Expected:

* HP decreases.

### Test 2

Repeat collisions.

Expected:

* HP eventually reaches zero.

### Test 3

Player reaches zero HP.

Expected:

* Player becomes inactive.

### Test 4

In multiplayer:

* Destroy Player 1.

Expected:

* Player 2 can continue playing.

### Test 5

Destroy all players.

Expected:

* GAME OVER appears.

### Test 6

After Game Over:

Expected:

* No new enemies spawn.
* No new waves start.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed work to tasks/completed.md.
3. Add the next milestone to tasks/current.md.

Do not modify architecture documents.
