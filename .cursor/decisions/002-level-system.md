# 002-level-system

## Status

Accepted

---

## Context

The game originally contained a single gameplay style:

* free movement
* screen wrapping
* enemies spawning from screen edges
* wave progression

A new gameplay segment is planned after Wave 3.

This segment introduces significantly different mechanics:

* players remain near the bottom of the screen
* enemies appear in formations
* enemies drop bombs
* enemies require multiple hits
* no screen wrapping

These mechanics differ substantially from Survival Mode.

Continuing to extend the existing WaveManager would increase complexity and create mode-specific conditionals throughout the codebase.

---

## Decision

Introduce a Level System.

The game owns exactly one active level.

Each level encapsulates:

* enemy spawning rules
* victory conditions
* gameplay-specific behaviours
* progression logic

The Game object delegates gameplay responsibilities to the active level.

---

## Proposed Structure

```text
Game
 └── LevelManager
      ├── SurvivalLevel
      └── FormationLevel
```

Each level implements a common interface.

Example responsibilities:

* initialize level
* update level
* spawn enemies
* determine completion
* determine failure

---

## Benefits

### Separation of Gameplay Rules

Survival Mode and Formation Mode can evolve independently.

Changes to one mode do not affect the other.

---

### Reduced Complexity

Avoid patterns such as:

```python
if wave > 3:
    use_formation_rules()
else:
    use_survival_rules()
```

which tend to spread throughout the codebase.

---

### Extensibility

Future levels can be added without modifying existing gameplay modes.

Examples:

* BossLevel
* EscortLevel
* AsteroidFieldLevel
* EndlessMode

---

### Better AI Collaboration

Level responsibilities are explicit.

AI agents can reason about individual levels without understanding every gameplay variation.

---

## Consequences

A Level abstraction must be introduced.

WaveManager becomes a Survival Mode concern rather than a global game concern.

Future gameplay features should belong to the appropriate level instead of the Game class whenever possible.

---

## Alternatives Considered

### Extend WaveManager

Rejected.

Reason:

Different gameplay modes would become tightly coupled and difficult to maintain.

---

### Create Separate Games

Rejected.

Reason:

The modes share:

* players
* rendering
* input
* bullets
* health system

A shared architecture provides greater reuse.

---

## Result

The project will use a Level-based architecture.

All future gameplay modes should be implemented as Levels managed by the LevelManager.
