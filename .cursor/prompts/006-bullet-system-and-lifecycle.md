# 006-bullet-system-and-lifecycle

## Goal

Implement a proper bullet system with lifecycle management.
Bullets should be automatically removed when they expire or leave the screen.
This milestone focuses on bullet management, cleanup, and stability of the projectile system.
Do not introduce enemies or collision damage logic or second player.

---

## Context

The game already supports:

* player movement with inertia
* screen wrapping
* automatic shooting
* bullet spawning with velocity

Currently bullets likely exist indefinitely, which can lead to performance issues and incorrect gameplay state.

A lifecycle system is required to manage bullet lifetime and cleanup.

---

## Requirements

## Bullet Lifecycle

Each bullet must have:

* spawn time OR lifetime timer
* position
* velocity
* speed (already defined)
* direction

---

### Lifetime Expiration

Bullets must be removed when:

* their lifetime exceeds `BULLET_LIFETIME_SECONDS` (recommended: 2–3 seconds)

OR

* they are marked as expired by the system

---

### Screen Bounds Removal (Optional but Recommended)

Bullets should also be removed when:

* they leave the visible screen area by a configurable margin (e.g. 100px buffer)

This prevents unnecessary off-screen processing.

---

## Update System

Create or extend a system responsible for:

* updating bullet positions
* checking lifetime expiration
* removing dead bullets safely

Ensure removal does not break iteration over bullet collections.

Use safe patterns:

* copy list
* deferred removal queue
* or filtering approach

---

## Data Integrity

When a bullet is removed:

* it must be fully removed from game state
* no references should remain in active systems
* no rendering should occur for expired bullets

---

## Performance Consideration

The system should:

* scale with increasing bullet count
* avoid unnecessary per-frame allocations where possible
* remain simple and predictable

---

## Architecture Notes

* Bullet logic should remain separate from Player logic
* Lifecycle management should not be inside rendering code
* Prefer a `BulletSystem` or centralized `EntityManager` responsibility

---

## Out of Scope

Do NOT implement:

* collision detection
* enemy interaction
* damage system
* scoring
* particle effects
* sound effects
* power-ups

---

## Acceptance Criteria

* Bullets are spawned correctly and move independently
* Bullets are removed after exceeding lifetime
* (Optional) Bullets are removed when leaving screen bounds
* No memory or list growth over time
* No visual artifacts from deleted bullets
* Shooting system continues working without interruption
