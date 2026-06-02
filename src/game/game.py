import pygame

from config.settings import (
    BACKGROUND_COLOR,
    TARGET_FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from entities.bullet import Bullet
from entities.player import Player
from game.player_setup import create_center_player
from game.starfield import Starfield
from systems.bullet_movement import update_bullets
from systems.bullet_render import draw_bullets
from systems.player_input import read_player_one_input
from systems.player_movement import update_player_movement
from systems.player_render import draw_player
from systems.player_screen_wrap import update_player_screen_wrap
from systems.player_shooting import update_player_shooting


class Game:
    def __init__(self) -> None:
        pygame.init()
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self._running = True
        self._starfield = Starfield(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._player: Player = create_center_player(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._bullets: list[Bullet] = []

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
        update_player_shooting(self._player, self._bullets, dt)
        update_bullets(self._bullets, dt)

    def _render(self) -> None:
        self._screen.fill(BACKGROUND_COLOR)
        self._starfield.draw(self._screen)
        draw_player(self._screen, self._player)
        draw_bullets(self._screen, self._bullets)
        pygame.display.flip()
