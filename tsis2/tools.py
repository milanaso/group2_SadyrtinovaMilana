
import pygame
from collections import deque


def draw_pencil(surface, start, end, color, width):
    pygame.draw.line(surface, color, start, end, width)


def draw_line(surface, start, end, color, width):
    pygame.draw.line(surface, color, start, end, width)


def draw_rectangle(surface, start, end, color, width):
    rect = pygame.Rect(start, end).normalize()
    if rect.width > 0 and rect.height > 0:
        pygame.draw.rect(surface, color, rect, width)


def draw_circle(surface, start, end, color, width):
    center = ((start[0] + end[0]) // 2,
              (start[1] + end[1]) // 2)
    radius = int(
        (((end[0] - start[0]) ** 2 +
          (end[1] - start[1]) ** 2) ** 0.5) / 2
    )
    if radius > 0:
        pygame.draw.circle(surface, color, center, radius, width)


def draw_square(surface, start, end, color, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    side = min(abs(dx), abs(dy))
    x = start[0] + (side if dx < 0 else 0)
    y = start[1] + (side if dy < 0 else 0)
    rect = pygame.Rect(x, y, side, side)
    pygame.draw.rect(surface, color, rect, width)


def draw_right_triangle(surface, start, end, color, width):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(surface, color, points, width)


def draw_equilateral_triangle(surface, start, end, color, width):
    dx = end[0] - start[0]
    height = int(abs(dx) * 0.866)
    direction = 1 if end[1] >= start[1] else -1

    points = [
        start,
        (end[0], start[1]),
        ((start[0] + end[0]) // 2,
         start[1] + direction * height)
    ]
    pygame.draw.polygon(surface, color, points, width)


def draw_rhombus(surface, start, end, color, width):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2

    points = [
        (center_x, start[1]),
        (end[0], center_y),
        (center_x, end[1]),
        (start[0], center_y)
    ]
    pygame.draw.polygon(surface, color, points, width)


def flood_fill(surface, position, new_color):
    x, y = position
    width, height = surface.get_size()

    if not (0 <= x < width and 0 <= y < height):
        return

    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    pixels = deque([(x, y)])
    surface.set_at((x, y), new_color)

    while pixels:
        px, py = pixels.popleft()

        for nx, ny in (
            (px + 1, py),
            (px - 1, py),
            (px, py + 1),
            (px, py - 1)
        ):
            if 0 <= nx < width and 0 <= ny < height:
                if surface.get_at((nx, ny)) == target_color:
                    surface.set_at((nx, ny), new_color)
                    pixels.append((nx, ny))


def draw_text(surface, text, position, color, font_size=28):
    font = pygame.font.Font(None, font_size)
    rendered = font.render(text, True, color)
    surface.blit(rendered, position)
