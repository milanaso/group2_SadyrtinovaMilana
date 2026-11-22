import pygame


class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 25
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.step = 20
        self.color = (220, 35, 35)

    def handle_key(self, key):
        new_x, new_y = self.x, self.y

        if key == pygame.K_LEFT:
            new_x -= self.step
        elif key == pygame.K_RIGHT:
            new_x += self.step
        elif key == pygame.K_UP:
            new_y -= self.step
        elif key == pygame.K_DOWN:
            new_y += self.step
        else:
            return

        # Ignore a move if any part of the circle would leave the window.
        if (self.radius <= new_x <= self.screen_width - self.radius
                and self.radius <= new_y <= self.screen_height - self.radius):
            self.x, self.y = new_x, new_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
