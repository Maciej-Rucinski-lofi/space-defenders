from dataclasses import dataclass
from enum import Enum, auto

from entities.player import Player
from systems.health import any_player_alive


class GamePhase(Enum):
    RUNNING = auto()
    GAME_OVER = auto()


@dataclass
class GameState:
    phase: GamePhase


def create_game_state() -> GameState:
    return GameState(phase=GamePhase.RUNNING)


def is_gameplay_active(game_state: GameState) -> bool:
    return game_state.phase is GamePhase.RUNNING


def update_game_state(game_state: GameState, players: list[Player]) -> None:
    if game_state.phase is GamePhase.GAME_OVER:
        return
    if not any_player_alive(players):
        game_state.phase = GamePhase.GAME_OVER
