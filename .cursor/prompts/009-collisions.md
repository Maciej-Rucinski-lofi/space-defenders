# 009-collisions

## Goal

Implement the first collision system in the game.
Bullets should be able to destroy enemies.
This milestone introduces the first gameplay interaction between entities.
Keep the implementation simple and reliable.
Do not implement player damage, scoring, or visual effects yet.

---

## Context

The game already includes:

* player movement
* automatic shooting
* bullet lifecycle management
* enemy spawning
* enemy movement behaviour

Currently bullets and enemies coexist but do not interact.

This milestone introduces collision detection and entity destruction.

---

## Requirements

## Collision Detection

Implement collision detection between:

* Bullet
* Enemy

Only bullet-enemy collisions should be handled in this milestone.

---

## Collision Shape

Use a simple collision model:

### Recommended

Circular collision bounds:

* bullet radius
* enemy radius

Collision occurs when:

distance(bullet, enemy) < combined_radius

No pixel-perfect collision detection.

Keep the system simple.

---

## Bullet Hits Enemy

When a bullet collides with an enemy:

### Bullet

* remove bullet from game

### Enemy

* remove enemy from game

Treat every hit as lethal.

Enemy health system is not required yet.

---

## Safe Entity Removal

Collision processing must safely remove entities.

Avoid:

* modifying collections while iterating

Use:

* removal queues
* deferred deletion
* filtered collections

Choose the approach that best fits the current architecture.

---

## Multiple Collision Handling

A bullet should only destroy:

* one enemy

After collision:

* bullet is removed
* no further collision checks for that bullet

---

## Debug Visualization (Optional)

Optional debug mode:

Display collision boundaries:

* bullet radius
* enemy radius

Useful for tuning hitboxes.

---

## Architecture Notes

Create a dedicated collision responsibility.

Examples:

* CollisionSystem
* CollisionManager

Avoid placing collision logic inside:

* rendering code
* player code
* enemy code

Collision detection should be centralized.

---

## Out of Scope

Do NOT implement:

* player damage
* enemy damage values
* health system
* score system
* particle effects
* explosion effects
* sounds
* power-ups
* game over logic

---

## Acceptance Criteria

* Bullets collide with enemies
* Enemy is removed after collision
* Bullet is removed after collision
* One bullet destroys one enemy
* No crashes occur during entity removal
* Collision detection works consistently
* No scoring or damage systems are introduced

---

## Manual Test Plan

### Test 1

* Fire at enemy.
* Enemy disappears.

### Test 2

* Bullet disappears after hit.

### Test 3

* Multiple enemies on screen.
* Bullet destroys only one target.

### Test 4

* Large number of bullets and enemies.
* No crashes or collection modification errors.

### Test 5

* Missed bullets continue normally until expiration.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed work to tasks/completed.md.
3. Add the next milestone to tasks/current.md.
