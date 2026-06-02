from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH
from entities.player import Player
from world.screen_wrap import wrap_position


def update_player_screen_wrap(player: Player) -> None:
    wrap_position(player.position, WINDOW_WIDTH, WINDOW_HEIGHT)
