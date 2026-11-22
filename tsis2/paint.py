
import pygame
import sys
from datetime import datetime

from tools import (
    draw_pencil,
    draw_line,
    draw_rectangle,
    draw_circle,
    draw_square,
    draw_right_triangle,
    draw_equilateral_triangle,
    draw_rhombus,
    flood_fill,
    draw_text
)


pygame.init()

WIDTH, HEIGHT = 1000, 700
TOOLBAR_WIDTH = 180
CANVAS_RECT = pygame.Rect(TOOLBAR_WIDTH, 0,
                          WIDTH - TOOLBAR_WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 - Paint Application")

clock = pygame.time.Clock()

canvas = pygame.Surface((CANVAS_RECT.width, CANVAS_RECT.height))
canvas.fill((255, 255, 255))

font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
DARK_GRAY = (70, 70, 70)
BLUE = (70, 130, 220)

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 165, 0),
    (255, 255, 0),
    (160, 32, 240),
    (255, 105, 180),
    (255, 255, 255)
]

tools = [
    "Pencil",
    "Line",
    "Rectangle",
    "Circle",
    "Square",
    "Right Triangle",
    "Equilateral Triangle",
    "Rhombus",
    "Eraser",
    "Fill",
    "Text",
    "Color Picker"
]

current_tool = "Pencil"
current_color = BLACK
brush_size = 2

drawing = False
start_pos = None
last_pos = None

text_active = False
text_input = ""
text_position = None


def canvas_position(pos):
    return pos[0] - TOOLBAR_WIDTH, pos[1]


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, TOOLBAR_WIDTH, HEIGHT))

    title = font.render("PAINT TOOLS", True, BLACK)
    screen.blit(title, (15, 10))

    for i, tool in enumerate(tools):
        y = 45 + i * 35
        rect = pygame.Rect(8, y, TOOLBAR_WIDTH - 16, 29)

        if current_tool == tool:
            pygame.draw.rect(screen, BLUE, rect)
            color = WHITE
        else:
            pygame.draw.rect(screen, WHITE, rect)
            color = BLACK

        label = small_font.render(tool, True, color)
        screen.blit(label, (15, y + 6))

    pygame.draw.line(screen, DARK_GRAY, (10, 475),
                     (170, 475), 2)

    screen.blit(small_font.render("Brush size:", True, BLACK),
                (15, 485))

    for i, size in enumerate([2, 5, 10]):
        rect = pygame.Rect(12 + i * 52, 515, 45, 30)
        if brush_size == size:
            pygame.draw.rect(screen, BLUE, rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)

        label = small_font.render(str(size), True, WHITE if brush_size == size else BLACK)
        screen.blit(label, (rect.x + 15, rect.y + 7))

    screen.blit(small_font.render("Colors:", True, BLACK), (15, 560))

    for i, color in enumerate(colors):
        x = 15 + (i % 4) * 38
        y = 585 + (i // 4) * 38
        pygame.draw.rect(screen, color, (x, y, 28, 28))
        pygame.draw.rect(screen, BLACK, (x, y, 28, 28), 1)

    pygame.draw.rect(screen, current_color, (75, 650, 30, 30))
    pygame.draw.rect(screen, BLACK, (75, 650, 30, 30), 1)


def save_canvas():
    filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, filename)
    print(f"Saved: {filename}")


def draw_preview():
    if not drawing or start_pos is None:
        return

    preview = canvas.copy()
    end_pos = canvas_position(pygame.mouse.get_pos())

    if current_tool == "Line":
        draw_line(preview, start_pos, end_pos,
                  current_color, brush_size)

    elif current_tool == "Rectangle":
        draw_rectangle(preview, start_pos, end_pos,
                       current_color, brush_size)

    elif current_tool == "Circle":
        draw_circle(preview, start_pos, end_pos,
                    current_color, brush_size)

    elif current_tool == "Square":
        draw_square(preview, start_pos, end_pos,
                    current_color, brush_size)

    elif current_tool == "Right Triangle":
        draw_right_triangle(preview, start_pos, end_pos,
                            current_color, brush_size)

    elif current_tool == "Equilateral Triangle":
        draw_equilateral_triangle(preview, start_pos, end_pos,
                                  current_color, brush_size)

    elif current_tool == "Rhombus":
        draw_rhombus(preview, start_pos, end_pos,
                     current_color, brush_size)

    screen.blit(preview, CANVAS_RECT.topleft)


running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, CANVAS_RECT.topleft)
    draw_toolbar()

    if drawing and current_tool != "Pencil":
        draw_preview()

    if text_active:
        preview_text = font.render(text_input + "|", True, current_color)
        screen.blit(preview_text, (text_position[0] + TOOLBAR_WIDTH,
                                   text_position[1]))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                if text_active:
                    text_active = False
                    text_input = ""
                else:
                    running = False

            elif text_active:
                if event.key == pygame.K_RETURN:
                    draw_text(canvas, text_input, text_position,
                              current_color)
                    text_active = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                elif event.unicode.isprintable():
                    text_input += event.unicode

            elif event.key == pygame.K_1:
                brush_size = 2

            elif event.key == pygame.K_2:
                brush_size = 5

            elif event.key == pygame.K_3:
                brush_size = 10

            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mx, my = event.pos

            if mx < TOOLBAR_WIDTH:

                for i, tool in enumerate(tools):
                    y = 45 + i * 35
                    if pygame.Rect(8, y, TOOLBAR_WIDTH - 16, 29).collidepoint(event.pos):
                        current_tool = tool

                for i, size in enumerate([2, 5, 10]):
                    rect = pygame.Rect(12 + i * 52, 515, 45, 30)
                    if rect.collidepoint(event.pos):
                        brush_size = size

                for i, color in enumerate(colors):
                    x = 15 + (i % 4) * 38
                    y = 585 + (i // 4) * 38
                    if pygame.Rect(x, y, 28, 28).collidepoint(event.pos):
                        current_color = color

            elif CANVAS_RECT.collidepoint(event.pos):

                pos = canvas_position(event.pos)

                if current_tool == "Fill":
                    flood_fill(canvas, pos, current_color)

                elif current_tool == "Text":
                    text_active = True
                    text_input = ""
                    text_position = pos

                elif current_tool == "Color Picker":
                    current_color = canvas.get_at(pos)[:3]

                elif current_tool in ("Pencil", "Eraser"):
                    drawing = True
                    last_pos = pos
                else:
                    drawing = True
                    start_pos = pos
        elif event.type == pygame.MOUSEMOTION and drawing:

                if current_tool in ("Pencil", "Eraser"):
                    pos = canvas_position(event.pos)

                if current_tool == "Eraser":
                    draw_pencil(canvas, last_pos, pos, WHITE, 20)
                else:
                    draw_pencil(canvas, last_pos, pos, current_color, brush_size)
                    last_pos = pos
                    

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            if drawing and start_pos is not None:
                end_pos = canvas_position(event.pos)

                if current_tool == "Line":
                    draw_line(canvas, start_pos, end_pos,
                              current_color, brush_size)

                elif current_tool == "Rectangle":
                    draw_rectangle(canvas, start_pos, end_pos,
                                   current_color, brush_size)

                elif current_tool == "Circle":
                    draw_circle(canvas, start_pos, end_pos,
                                current_color, brush_size)

                elif current_tool == "Square":
                    draw_square(canvas, start_pos, end_pos,
                                current_color, brush_size)

                elif current_tool == "Right Triangle":
                    draw_right_triangle(canvas, start_pos, end_pos,
                                        current_color, brush_size)

                elif current_tool == "Equilateral Triangle":
                    draw_equilateral_triangle(canvas, start_pos, end_pos,
                                              current_color, brush_size)

                elif current_tool == "Rhombus":
                    draw_rhombus(canvas, start_pos, end_pos,
                                 current_color, brush_size)

            drawing = False
            start_pos = None
            last_pos = None

    clock.tick(60)


pygame.quit()
sys.exit()
