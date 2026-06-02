# 001-create-project-and-window

## Goal

Create the initial project structure for a local multiplayer space shooter game using Python and Pygame.
This is the first milestone of the project.
Only implement project setup and a working game window.
Do not implement player movement, shooting, enemies, collisions, or game logic yet.

---

## Context

The game is a cooperative local multiplayer game.
Two players control spacecraft and fight incoming enemy ships.
The project follows the rules defined in:

* global.mdc
* architecture.mdc
* coding_standards.mdc
* game_design.mdc

Follow all project rules.

---

## Requirements

### Project Structure

Create the initial directory structure:

```text
src/
├── game/
├── entities/
├── systems/
├── config/
└── main.py
```

Create `__init__.py` files where appropriate.

### Configuration

Create a configuration module containing:

* window width
* window height
* window title
* target FPS

Use constants.

### Game Class

Create a Game class responsible for:

* initializing pygame
* creating the window
* managing the main loop
* handling quit events
* controlling FPS

No gameplay logic should exist inside main.py.

### Main Entry Point

Create a minimal entry point that starts the Game instance.

### Window

Display a window with:

* black background looks like space
* stars as small white dots put randomly
* project title in window caption

The application must close correctly when the user exits or press ESC button.

---

## Out of Scope

Do NOT implement:

* player ships
* enemies
* bullets
* collisions
* AI
* waves
* HUD
* sounds
* assets

---

## Acceptance Criteria

* Project runs successfully using Python.
* A pygame window opens.
* Window title is visible.
* Black background is rendered.
* Closing the window exits cleanly.
* Main loop runs at configured FPS.
* Game logic is encapsulated inside a Game class.
* No gameplay entities exist yet.

---

## Documentation Updates

After implementation:

1. Update `context/current_state.md`.
2. Mark this milestone as completed in `tasks/completed.md`.
3. Add the next recommended task to `tasks/current.md`.
4. Remove appropriate task from `tasks/backlog.md`.

Do not modify architecture documents.
