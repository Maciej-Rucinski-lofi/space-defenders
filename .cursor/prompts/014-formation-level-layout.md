# 014-formation-level-layout

## Goal

Create the visual and gameplay layout of Formation Mode.

This milestone establishes the playfield structure and player movement rules.

Do not implement enemy formations, bombs, or enemy combat yet.

The objective is to make Formation Mode feel fundamentally different from Survival Mode.

---

## Context

The game now supports multiple level types through the Level System.

Formation Mode is inspired by classic arcade space shooters.

Examples:

* Galaxy Attack
* Galaga
* Space Invaders

Players fight organized enemy formations from the bottom of the screen.

---

## Requirements

## Automatic Transition

When Survival Mode is completed:

* LevelManager should transition to FormationLevel

Recommended trigger:

```text
Survival Wave 3 completed
    ↓
FormationLevel starts
```

Transition should be managed through the LevelManager.

---

## Formation Mode Play Area

Formation Mode uses a different movement model.

Differences from Survival Mode:

* no screen wrapping
* no free movement across the entire map
* no Asteroids-style inertia

Players operate inside a limited area near the bottom of the screen.

---

## Player Movement Rules

Players should be positioned near the bottom of the screen.

Movement:

* left
* right

Optional:

* limited up/down movement inside player zone

Recommended first implementation:

```text
Horizontal movement only
```

---

## Remove Asteroids Physics

During Formation Mode:

* disable rotation
* disable thrust
* disable inertia

Players should immediately respond to movement input.

Movement should feel arcade-like.

---

## Player Area

Define a player zone.

Example:

```text
Top of Player Zone
------------------


Player Area


Bottom of Screen
```

Players cannot leave this zone.

Movement should be clamped to valid boundaries.

---

## Shooting

Players continue to shoot automatically.

Existing shooting system should remain active.

Bullets should travel upward.

No gameplay changes to bullets are required yet.

---

## Background Separation

Formation Mode should be visually distinguishable from Survival Mode.

Simple options:

* different background color
* background should move slowly vertically - spacecraft looks like moving in space upwards
* different starfield pattern
* Formation Mode label

Keep implementation simple.

---

## Temporary Enemy Placeholder

Until enemy formations are implemented:

* spawn a small number of placeholder enemies
  OR
* display a debug message

The level should not appear empty.

No formation logic is required yet.

---

## Architecture Notes

Formation Mode should define:

* player movement rules
* play area constraints
* level-specific setup

Existing systems should be reused where possible.

Avoid duplicating player implementations.

---

## Out of Scope

Do NOT implement:

* enemy formations
* formation movement
* enemy bombs
* enemy health changes
* boss enemies
* score system
* Formation Mode victory conditions

These features belong to future milestones.

---

## Acceptance Criteria

* FormationLevel starts after Survival completion
* Players appear near the bottom of the screen
* Players cannot leave the player zone
* No screen wrapping occurs
* No Asteroids-style inertia is present
* Movement feels immediate and arcade-like
* Automatic shooting continues working
* Formation Mode looks visually different from Survival Mode
* Existing architecture remains intact

---

## Manual Test Plan

### Test 1

Complete Survival Mode.

Expected:

* FormationLevel starts automatically.

### Test 2

Move players.

Expected:

* Immediate left/right movement.
* No inertia.

### Test 3

Attempt to leave player area.

Expected:

* Movement is constrained.

### Test 4

Observe shooting.

Expected:

* Automatic shooting continues working.

### Test 5

Observe visuals.

Expected:

* Formation Mode is visually distinguishable from Survival Mode.

---

## Documentation Updates

After implementation:

1. Update formation_mode.md.
2. Update context/current_state.md.
3. Move completed task to tasks/completed.md.
4. Add the next milestone to tasks/current.md.

Do not modify Survival Mode gameplay.
