# Survival Mode

## Purpose

Survival Mode is the first game mode.
Players survive consecutive waves of enemies while moving freely in open space.
This mode introduces the core mechanics of the game and serves as the primary progression path before special levels become available.

---

## Player Experience

Players control small spacecraft.

Movement is inspired by Asteroids:

* rotation-based movement
* forward thrust
* inertia
* no friction
* screen wrapping

Players can move freely across the entire play area.

---

## Objectives

The objective is to survive and clear enemy waves.

A wave is completed when:

1. All enemies have been spawned.
2. All spawned enemies have been destroyed.

After a short intermission, the next wave begins.

---

## Enemy Behaviour

Enemies:

* spawn from screen edges
* move toward players
* may have small movement variations
* can collide with players
* are destroyed by player bullets

Enemy formations are not used in this mode.

Enemies operate independently.

---

## Combat Rules

Players automatically fire bullets.

Bullets:

* travel in the direction of ship rotation
* have limited lifetime
* destroy enemies on impact

Enemy-player collisions:

* damage players
* destroy the enemy

---

## Wave Progression

Wave 1:

* 5 enemies

Wave 2:

* 8 enemies

Wave 3:

* 11 enemies

Enemy count increases with each wave.

---

## Transition Rules

After Wave 3 is completed:

* Survival Mode ends
* Formation Mode begins

The transition is managed by the Level Manager.

Survival Mode should not directly start Formation Mode.

Instead, it signals completion to the Level Manager.

---

## Responsibilities

Survival Mode manages:

* wave progression
* enemy spawning
* wave completion checks
* survival-specific victory conditions

Survival Mode does NOT manage:

* game state transitions
* rendering infrastructure
* player input systems
* Formation Mode logic

---

## Success Condition

The mode is completed when:

* Wave 3 is cleared

---

## Failure Condition

The mode fails when:

* all players are destroyed
