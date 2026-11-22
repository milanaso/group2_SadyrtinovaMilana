import pygame

from player import MusicPlayer


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 420))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()
    player = MusicPlayer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False
                elif event.key == pygame.K_p:
                    player.toggle_play_pause()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()

        screen.fill((25, 28, 38))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    player.stop()
    pygame.quit()


if __name__ == "__main__":
    main()
