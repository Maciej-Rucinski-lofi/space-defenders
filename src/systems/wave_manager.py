from dataclasses import dataclass
from enum import Enum, auto

from config.wave import (
    INTERMISSION_DURATION_S,
    WAVE_ANNOUNCEMENT_DURATION_S,
    WAVE_PREP_DURATION_S,
    enemies_for_wave,
)


class WavePhase(Enum):
    ANNOUNCING = auto()
    PREPARING = auto()
    SPAWNING = auto()
    INTERMISSION = auto()


@dataclass
class WaveManager:
    wave_number: int
    enemies_remaining_to_spawn: int
    phase: WavePhase
    phase_timer_remaining: float


def create_wave_manager() -> WaveManager:
    return WaveManager(
        wave_number=1,
        enemies_remaining_to_spawn=enemies_for_wave(1),
        phase=WavePhase.ANNOUNCING,
        phase_timer_remaining=WAVE_ANNOUNCEMENT_DURATION_S,
    )


def is_spawn_allowed(wave_manager: WaveManager) -> bool:
    return (
        wave_manager.phase is WavePhase.SPAWNING
        and wave_manager.enemies_remaining_to_spawn > 0
    )


def record_enemy_spawned(wave_manager: WaveManager) -> None:
    if wave_manager.enemies_remaining_to_spawn > 0:
        wave_manager.enemies_remaining_to_spawn -= 1


def enemies_remaining_in_wave(
    wave_manager: WaveManager, active_enemy_count: int
) -> int:
    return wave_manager.enemies_remaining_to_spawn + active_enemy_count


def _begin_announcement(wave_manager: WaveManager) -> None:
    wave_manager.phase = WavePhase.ANNOUNCING
    wave_manager.phase_timer_remaining = WAVE_ANNOUNCEMENT_DURATION_S


def _begin_preparation(wave_manager: WaveManager) -> None:
    wave_manager.phase = WavePhase.PREPARING
    wave_manager.phase_timer_remaining = WAVE_PREP_DURATION_S


def _begin_spawning(wave_manager: WaveManager) -> None:
    wave_manager.phase = WavePhase.SPAWNING
    wave_manager.phase_timer_remaining = 0.0


def _start_next_wave(wave_manager: WaveManager) -> None:
    wave_manager.wave_number += 1
    wave_manager.enemies_remaining_to_spawn = enemies_for_wave(
        wave_manager.wave_number
    )
    _begin_announcement(wave_manager)


def _begin_intermission(wave_manager: WaveManager) -> None:
    wave_manager.phase = WavePhase.INTERMISSION
    wave_manager.phase_timer_remaining = INTERMISSION_DURATION_S


def _advance_from_timed_phase(wave_manager: WaveManager) -> None:
    if wave_manager.phase is WavePhase.INTERMISSION:
        _start_next_wave(wave_manager)
    elif wave_manager.phase is WavePhase.ANNOUNCING:
        _begin_preparation(wave_manager)
    elif wave_manager.phase is WavePhase.PREPARING:
        _begin_spawning(wave_manager)


def update_wave_manager(
    wave_manager: WaveManager,
    active_enemy_count: int,
    dt: float,
) -> None:
    if wave_manager.phase is not WavePhase.SPAWNING:
        wave_manager.phase_timer_remaining -= dt
        if wave_manager.phase_timer_remaining <= 0:
            _advance_from_timed_phase(wave_manager)
        return

    if (
        wave_manager.enemies_remaining_to_spawn == 0
        and active_enemy_count == 0
    ):
        _begin_intermission(wave_manager)
