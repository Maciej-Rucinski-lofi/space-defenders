# 008-enemy-behaviour-and-variation

## Goal

Enhance enemy behaviour beyond simple movement toward the player.
Enemies should feel less deterministic and more like real threats rather than homing drones.
This milestone focuses on behaviour variation, steering, and simple combat readiness preparation.
Do not implement collision damage or scoring yet.

---

## Context

The game already includes:

* player movement with inertia
* automatic shooting
* bullet system
* enemy spawning from edges
* enemies moving toward players

Current issue:

Enemies behave too uniformly:

* all move directly toward player
* no variation
* predictable trajectories

This milestone improves gameplay feel without adding new systems.

---

## Requirements

## 1. Movement Variation

Enemies must NOT move in a perfectly straight line toward the player at all times.

Introduce at least one of the following:

### Option A (recommended): Steering Offset

Add slight directional offset:

* target direction = direction_to_player + small_random_vector
* recompute periodically (e.g. every 0.5–1.5s)

---

### Option B: Drift Behaviour

Enemies slightly drift sideways while moving forward:

* base direction = toward player
* add perpendicular oscillation (sin-like or random jitter)

---

## 2. Behaviour Re-evaluation

Enemies should not lock direction forever.

Add behaviour update interval:

* every 0.5–2 seconds:

  * reselect target direction OR
  * adjust steering offset

This creates less robotic movement.

---

## 3. Enemy Roles (Light Variation)

Introduce minimal enemy types (no full system yet):

### Type 1: Chaser

* direct pursuit
* medium speed

### Type 2: Drifter

* slower
* higher movement offset randomness

### Type 3: Fast Kamikaze

* fast
* high steering instability
* no shooting

Types can be hardcoded at spawn for now.

---

## 4. Visual Debug Option (Optional but useful)

Add optional debug mode:

* draw enemy target direction line
* visualize current velocity vector

This helps tune AI behaviour.

---

## Architecture Notes

* Keep behaviour logic in enemy system, not spawn system
* Avoid coupling behaviour with rendering
* Keep randomness configurable (seeded if possible)

---

## Out of Scope

Do NOT implement:

* collision damage
* scoring system
* enemy shooting
* wave system changes
* pathfinding
* obstacle avoidance
* advanced AI state machines

---

## Acceptance Criteria

* Enemies no longer move in perfectly straight lines toward player
* Movement has visible variation or drift
* Behaviour changes over time (not static)
* Multiple enemy types exist with different movement styles
* System remains simple and deterministic enough for debugging
* No new gameplay systems beyond movement behaviour
