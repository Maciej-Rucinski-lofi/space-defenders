import pygame

from config.player import create_center_player
from config.settings import TARGET_FPS, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from entities.player import Player
from game.starfield import Starfield
from systems.player_input import read_player_one_input
from systems.player_movement import update_player_movement
from systems.player_render import draw_player
from systems.player_screen_wrap import update_player_screen_wrap

BACKGROUND_COLOR = (0, 0, 0)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self._running = True
        self._starfield = Starfield(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._player: Player = create_center_player(WINDOW_WIDTH, WINDOW_HEIGHT)

    def run(self) -> None:
        while self._running:
            dt = self._clock.tick(TARGET_FPS) / 1000.0
            self._handle_events()
            self._update(dt)
            self._render()
        pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False

    def _update(self, dt: float) -> None:
        player_input = read_player_one_input()
        update_player_movement(self._player, player_input, dt)
        update_player_screen_wrap(self._player)

    def _render(self) -> None:
        self._screen.fill(BACKGROUND_COLOR)
        self._starfield.draw(self._screen)
        draw_player(self._screen, self._player)
        pygame.display.flip()
