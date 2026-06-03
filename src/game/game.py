import pygame

from config.settings import (
    BACKGROUND_COLOR,
    TARGET_FPS,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from entities.bullet import Bullet
from entities.enemy import Enemy
from entities.player import Player
from game.player_setup import create_center_player
from game.starfield import Starfield
from systems.bullet_system import update_bullets
from systems.bullet_render import draw_bullets
from config.enemy_behaviour import ENEMY_AI_DEBUG
from systems.collision import process_bullet_enemy_collisions
from systems.collision_debug_render import draw_collision_debug
from systems.enemy_debug_render import draw_enemy_debug
from systems.enemy_movement import update_enemies
from systems.enemy_render import draw_enemies
from systems.enemy_spawner import create_enemy_spawner, update_enemy_spawner
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
        self._enemies: list[Enemy] = []
        self._enemy_spawner = create_enemy_spawner()
        self._enemy_ai_debug = ENEMY_AI_DEBUG

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                elif event.key == pygame.K_F3:
                    self._enemy_ai_debug = not self._enemy_ai_debug

    def _update(self, dt: float) -> None:
        player_input = read_player_one_input()
        update_player_movement(self._player, player_input, dt)
        update_player_screen_wrap(self._player)
        update_player_shooting(self._player, self._bullets, dt)
        update_bullets(self._bullets, dt)
        update_enemy_spawner(
            self._enemy_spawner, self._enemies, self._player, dt
        )
        update_enemies(self._enemies, self._player, dt)
        process_bullet_enemy_collisions(self._bullets, self._enemies)

    def _render(self) -> None:
        self._screen.fill(BACKGROUND_COLOR)
        self._starfield.draw(self._screen)
        draw_player(self._screen, self._player)
        draw_bullets(self._screen, self._bullets)
        draw_enemies(self._screen, self._enemies)
        if self._enemy_ai_debug:
            draw_collision_debug(self._screen, self._bullets, self._enemies)
            draw_enemy_debug(self._screen, self._enemies, self._player.position)
        pygame.display.flip()
