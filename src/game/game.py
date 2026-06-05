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
from game.player_setup import create_center_player, first_alive_player
from game.starfield import Starfield
from systems.bullet_system import update_bullets
from systems.bullet_render import draw_bullets
from config.enemy_behaviour import ENEMY_AI_DEBUG
from systems.collision import (
    process_bullet_enemy_collisions,
    process_enemy_player_collisions,
)
from systems.collision_debug_render import draw_collision_debug
from systems.enemy_debug_render import draw_enemy_debug
from systems.enemy_movement import update_enemies
from systems.enemy_render import draw_enemies
from systems.enemy_spawner import create_enemy_spawner, update_enemy_spawner
from systems.game_over_render import draw_game_over
from systems.game_state import (
    create_game_state,
    is_gameplay_active,
    update_game_state,
)
from systems.health_render import draw_health_hud
from systems.wave_manager import (
    create_wave_manager,
    is_spawn_allowed,
    record_enemy_spawned,
    update_wave_manager,
)
from systems.wave_render import draw_wave_announcement, draw_wave_hud
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
        self._players: list[Player] = [
            create_center_player(WINDOW_WIDTH, WINDOW_HEIGHT)
        ]
        self._bullets: list[Bullet] = []
        self._enemies: list[Enemy] = []
        self._enemy_spawner = create_enemy_spawner()
        self._wave_manager = create_wave_manager()
        self._game_state = create_game_state()
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

    def _update_players(self, dt: float) -> None:
        player_input = read_player_one_input()
        for player in self._players:
            update_player_movement(player, player_input, dt)
            update_player_screen_wrap(player)
            update_player_shooting(player, self._bullets, dt)

    def _update(self, dt: float) -> None:
        if not is_gameplay_active(self._game_state):
            return

        self._update_players(dt)
        update_bullets(self._bullets, dt)
        target = first_alive_player(self._players)
        spawned = update_enemy_spawner(
            self._enemy_spawner,
            self._enemies,
            target,
            dt,
            is_spawn_allowed(self._wave_manager),
        )
        if spawned:
            record_enemy_spawned(self._wave_manager)
        update_enemies(self._enemies, target, dt)
        process_bullet_enemy_collisions(self._bullets, self._enemies)
        process_enemy_player_collisions(self._enemies, self._players)
        update_wave_manager(self._wave_manager, len(self._enemies), dt)
        update_game_state(self._game_state, self._players)

    def _render(self) -> None:
        self._screen.fill(BACKGROUND_COLOR)
        self._starfield.draw(self._screen)
        for player in self._players:
            draw_player(self._screen, player)
        draw_bullets(self._screen, self._bullets)
        draw_enemies(self._screen, self._enemies)
        draw_wave_announcement(self._screen, self._wave_manager)
        draw_wave_hud(self._screen, self._wave_manager, len(self._enemies))
        draw_health_hud(self._screen, self._players)
        draw_game_over(
            self._screen,
            self._game_state,
            self._wave_manager.wave_number,
        )
        if self._enemy_ai_debug:
            draw_collision_debug(self._screen, self._bullets, self._enemies)
            target = first_alive_player(self._players)
            if target is not None:
                draw_enemy_debug(
                    self._screen, self._enemies, target.position
                )
        pygame.display.flip()
