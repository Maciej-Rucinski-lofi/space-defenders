# 004-max-player-velocity

## Goal

Introduce a maximum velocity limit for the player ship.
The ship should not accelerate infinitely when thrust is applied.
This milestone only adjusts movement constraints.
Do not implement new gameplay systems.

---

## Context

The player movement system already supports:

* rotation
* thrust-based acceleration
* inertia (no friction)

Currently, continuous thrust allows velocity to grow indefinitely, which leads to uncontrollable movement.
A velocity cap is required to keep gameplay readable and balanced.
Follow all project rules and existing architecture.

---

## Requirements

### Maximum Speed

Introduce a constant:

* `MAX_PLAYER_SPEED`

This value defines the maximum allowed magnitude of player velocity.

Recommended initial value:
* 250–400 units/second (tunable)

---

### Velocity Clamping

After applying thrust and physics updates:

* compute velocity magnitude
* if magnitude exceeds MAX_PLAYER_SPEED:
  * clamp velocity vector to MAX_PLAYER_SPEED while preserving direction

---

### Behaviour

* Player can still accelerate normally up to the limit
* Player retains inertia
* Player cannot exceed maximum speed
* Direction of movement must remain unaffected by clamping

---

### Implementation Note

Clamping should be applied in the movement system, not inside input handling.
Keep separation of concerns:
* Input → applies force
* Movement system → applies physics + constraints

---

## Out of Scope

Do NOT implement:

* friction
* drag
* enemy systems
* shooting
* collisions
* screen wrapping changes
* UI changes

---

## Acceptance Criteria

* Player accelerates when thrust is held
* Player velocity stops increasing after reaching MAX_PLAYER_SPEED
* Movement direction remains smooth and natural
* Rotation is unaffected
* No jitter or sudden snapping occurs
* System remains frame-rate independent

---
