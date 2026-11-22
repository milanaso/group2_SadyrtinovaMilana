import pygame

from clock import MickeyClock


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Mickey's Clock")
    clock = pygame.time.Clock()
    mickey_clock = MickeyClock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        mickey_clock.update()
        screen.fill((245, 245, 245))
        mickey_clock.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
