# 002-player-movement

## Goal

Implement the first playable player ship with Asteroids-style movement.
The player should be able to rotate the ship and accelerate forward using thrust.
This milestone focuses only on movement and basic rendering.
Do not implement shooting, enemies, collisions, or multiplayer yet.

---

## Context

The game is a cooperative local multiplayer space shooter.
Ships move in open space.
Movement should feel similar to classic Asteroids:

* rotation-based movement
* forward thrust
* inertia
* no friction

The ship continues moving after thrust is released.
Follow all project rules and architecture documents.

---

## Requirements

### Player Entity

Create a Player entity.

The entity should contain state only.

Store at minimum:

* position
* velocity
* rotation
* rotation speed
* thrust force

Use appropriate vector types where possible.

---

## Rendering

Render a simple placeholder ship.
Do not use external assets.
Use a simple geometric shape:

* triangle
* polygon
* wireframe-style ship

The ship should visually rotate according to its current rotation.

---

## Controls

Player 1 controls:

* left arrow = rotate left
* right arrow = rotate right
* up arrow = thrust forward

Input handling should be separated from entity state where practical.

---

## Movement

Implement:

### Rotation

* left arrow rotates counter-clockwise
* right arrow rotates clockwise

### Thrust

When Up arrow is pressed:

* apply acceleration in the direction the ship is facing

### Inertia

When thrust is released:
* the ship keeps moving

### Delta Time

Movement must be frame-rate independent.
Use delta time for all movement calculations.

---

## Initial Spawn

Spawn the player ship at the center of the screen.

Initial values:

* zero velocity
* facing left

---

## Out of Scope

Do NOT implement:

* shooting
* bullets
* enemies
* collisions
* health
* multiple players
* screen wrapping
* wave system
* UI

---

## Acceptance Criteria

* A ship is visible on screen.
* The ship spawns in the center.
* left arrow rotates left.
* right arrow rotates right.
* up arrow accelerates the ship forward.
* Releasing up arrow does not stop movement.
* Movement uses delta time.
* Ship orientation matches rendered rotation.
* No gameplay systems beyond movement are implemented.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed tasks to tasks/completed.md.
3. Add the next milestone to tasks/current.md.

Do not modify architecture documents.
