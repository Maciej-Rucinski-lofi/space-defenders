# 003-screen-wrapping

## Goal

Implement screen wrapping for the player ship.
When the ship leaves one side of the screen, it should immediately appear on the opposite side while preserving its velocity and rotation.
This milestone focuses only on screen wrapping.
Do not implement shooting, enemies, collisions, or multiplayer.

---

## Context

The game uses Asteroids-style movement.
The game world is topologically continuous.
There are no solid screen boundaries.
When an object exits the visible area, it reappears on the opposite side.
The player's movement system is already implemented.
Follow all project rules and architecture documents.

---

## Requirements

### Screen Wrapping

Implement wrapping for the player ship.

#### Horizontal

If the ship moves beyond the left edge:
* appear on the right edge

If the ship moves beyond the right edge:
* appear on the left edge

#### Vertical

If the ship moves beyond the top edge:
* appear on the bottom edge

If the ship moves beyond the bottom edge:
* appear on the top edge

---

## Preserve State

Wrapping must not modify:

* velocity
* rotation
* acceleration state

The ship should continue moving naturally after wrapping.

---

## Configuration

Do not hardcode screen dimensions.
Use values from the configuration module.

---

## Architecture

Wrapping logic should not be implemented directly inside rendering code.
Keep responsibilities separated according to architecture.mdc.
Prefer a dedicated utility, system, or game-world responsibility if it fits the current architecture.

---

## Visual Behaviour

Example:

1. Ship accelerates toward the right edge.
2. Ship leaves the visible screen.
3. Ship instantly appears at the left edge.
4. Movement continues smoothly.

The player should perceive the world as continuous.

---

## Out of Scope

Do NOT implement:

* bullets
* bullet wrapping
* enemies
* enemy wrapping
* shooting
* health
* UI
* multiplayer
* collision detection

Only the player ship should support wrapping in this milestone.

---

## Acceptance Criteria

* Ship wraps correctly from left to right.
* Ship wraps correctly from right to left.
* Ship wraps correctly from top to bottom.
* Ship wraps correctly from bottom to top.
* Velocity is preserved after wrapping.
* Rotation is preserved after wrapping.
* No visible pauses occur during wrapping.
* Screen dimensions come from configuration.
* No unrelated gameplay systems are introduced.

---

## Manual Test Plan

Verify the following scenarios:

### Test 1

* Accelerate toward the right edge.
* Ship appears on the left side.

### Test 2

* Accelerate toward the left edge.
* Ship appears on the right side.

### Test 3

* Accelerate toward the top edge.
* Ship appears on the bottom side.

### Test 4

* Accelerate toward the bottom edge.
* Ship appears on the top side.

### Test 5

* Wrap while rotating.
* Rotation remains unchanged.

### Test 6

* Wrap at high speed.
* Movement remains smooth.

---

## Documentation Updates

After implementation:

1. Update context/current_state.md.
2. Move completed work to tasks/completed.md.
3. Add the next milestone to tasks/current.md.

Do not modify architecture documents.
