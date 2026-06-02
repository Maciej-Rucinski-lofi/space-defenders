from pygame.math import Vector2


def wrap_position(position: Vector2, width: float, height: float) -> None:
    if position.x < 0:
        position.x += width
    elif position.x >= width:
        position.x -= width
    if position.y < 0:
        position.y += height
    elif position.y >= height:
        position.y -= height
