import json
from dataclasses import dataclass
from pathlib import Path

PLAYER_NAMES_FILENAME = "player_names.json"
DEFAULT_PLAYER_ONE_NAME = "P1"
DEFAULT_PLAYER_TWO_NAME = "P2"


@dataclass(frozen=True)
class PlayerNames:
    player_one: str
    player_two: str


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def player_names_path() -> Path:
    return _project_root() / PLAYER_NAMES_FILENAME


def _normalize_name(value: object, fallback: str) -> str:
    if not isinstance(value, str):
        return fallback
    name = value.strip()
    return name if name else fallback


def load_player_names() -> PlayerNames:
    path = player_names_path()
    if not path.is_file():
        return PlayerNames(DEFAULT_PLAYER_ONE_NAME, DEFAULT_PLAYER_TWO_NAME)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return PlayerNames(DEFAULT_PLAYER_ONE_NAME, DEFAULT_PLAYER_TWO_NAME)
    if not isinstance(data, dict):
        return PlayerNames(DEFAULT_PLAYER_ONE_NAME, DEFAULT_PLAYER_TWO_NAME)
    return PlayerNames(
        player_one=_normalize_name(data.get("player1"), DEFAULT_PLAYER_ONE_NAME),
        player_two=_normalize_name(data.get("player2"), DEFAULT_PLAYER_TWO_NAME),
    )
