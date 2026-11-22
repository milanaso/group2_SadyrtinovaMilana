from datetime import datetime
from pathlib import Path

import pygame


class MickeyClock:
    def __init__(self):
        self.center = (350, 390)
        self.face_radius = 175
        image_path = Path(__file__).parent / "images" / "mickey_hand.png"
        self.hand_image = pygame.image.load(str(image_path)).convert_alpha()
        self.hand_image = pygame.transform.smoothscale(self.hand_image, (18, 150))
        self.font = pygame.font.Font(None, 30)
        self.minute_angle = 0
        self.second_angle = 0
        self.time_text = ""

    def update(self):
        now = datetime.now()
        self.minute_angle = (now.minute + now.second / 60) * 6
        self.second_angle = now.second * 6
        self.time_text = now.strftime("%H:%M:%S")

    def draw_hand(self, surface, angle, length, color):
        hand = pygame.transform.smoothscale(self.hand_image, (18, length))
        rotated = pygame.transform.rotate(hand, -angle)
        pivot = pygame.Vector2(self.center)
        original_pivot = pygame.Vector2(hand.get_width() / 2, hand.get_height())
        offset = pygame.Vector2(rotated.get_width() / 2, rotated.get_height())
        rotated_pivot = pygame.Vector2(rotated.get_rect().center)
        rotated_pivot.y += rotated.get_height() / 2 - original_pivot.y
        rotated_pivot = pygame.Vector2(rotated.get_width() / 2, rotated.get_height() / 2)
        radians = pygame.math.Vector2(0, -length / 2).rotate(angle)
        rect = rotated.get_rect(center=(self.center[0] + radians.x,
                                        self.center[1] + radians.y))
        surface.blit(rotated, rect)

    def draw(self, surface):
        pygame.draw.circle(surface, (25, 25, 25), (220, 205), 95)
        pygame.draw.circle(surface, (25, 25, 25), (480, 205), 95)
        pygame.draw.circle(surface, (25, 25, 25), self.center, self.face_radius)
        pygame.draw.circle(surface, (255, 255, 255), self.center, self.face_radius - 12)

        for number in range(12):
            angle = math_angle = number * 30
            import math
            radians = math.radians(math_angle - 90)
            start = (self.center[0] + 145 * math.cos(radians),
                     self.center[1] + 145 * math.sin(radians))
            end = (self.center[0] + 160 * math.cos(radians),
                   self.center[1] + 160 * math.sin(radians))
            pygame.draw.line(surface, (35, 35, 35), start, end, 5)

        self.draw_hand(surface, self.minute_angle, 115, (30, 30, 30))
        self.draw_hand(surface, self.second_angle, 145, (210, 40, 40))
        pygame.draw.circle(surface, (30, 30, 30), self.center, 11)

        text = self.font.render(self.time_text, True, (20, 20, 20))
        surface.blit(text, text.get_rect(center=(350, 625)))
        hint = pygame.font.Font(None, 23).render("ESC — quit", True, (90, 90, 90))
        surface.blit(hint, hint.get_rect(center=(350, 660)))
