from pathlib import Path
import pygame


class MusicPlayer:
    SUPPORTED_FORMATS = {".mp3", ".wav", ".ogg"}

    def __init__(self):
        pygame.mixer.init()
        self.music_folder = Path(__file__).parent / "music"
        self.tracks = sorted(
            path for path in self.music_folder.iterdir()
            if path.is_file() and path.suffix.lower() in self.SUPPORTED_FORMATS
        )
        self.current_index = 0
        self.paused = False
        self.started = False
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)
        self.status = "Add audio files to music_player/music"

    @property
    def current_track(self):
        if not self.tracks:
            return None
        return self.tracks[self.current_index]

    def play(self):
        track = self.current_track
        if track is None:
            self.status = "No tracks found — add MP3, WAV, or OGG files"
            return
        try:
            pygame.mixer.music.load(str(track))
            pygame.mixer.music.play()
            self.paused = False
            self.started = True
            self.status = "Playing"
        except pygame.error as error:
            self.status = f"Cannot play this file: {error}"

    def toggle_play_pause(self):
        if self.current_track is None:
            self.status = "Playlist is empty"
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.status = "Playing"
        elif self.started and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True
            self.status = "Paused"
        else:
            self.play()

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False
        self.started = False
        self.status = "Stopped"

    def next_track(self):
        if self.tracks:
            self.current_index = (self.current_index + 1) % len(self.tracks)
            self.play()

    def previous_track(self):
        if self.tracks:
            self.current_index = (self.current_index - 1) % len(self.tracks)
            self.play()

    def draw(self, screen):
        title = self.font.render("PYGAME MUSIC PLAYER", True, (245, 245, 255))
        screen.blit(title, (35, 35))

        if self.current_track:
            track_name = self.current_track.name
        else:
            track_name = "No track selected"
        name = self.small_font.render(track_name, True, (180, 210, 255))
        screen.blit(name, (35, 110))

        status = self.small_font.render(self.status, True, (220, 220, 220))
        screen.blit(status, (35, 155))

        if self.tracks:
            position_ms = max(0, pygame.mixer.music.get_pos())
            seconds = position_ms // 1000
            time_label = self.small_font.render(
                f"Position: {seconds // 60:02}:{seconds % 60:02}",
                True, (220, 220, 220)
            )
            screen.blit(time_label, (35, 205))
            pygame.draw.rect(screen, (75, 80, 95), (35, 250, 620, 10), border_radius=5)
            # pygame.mixer.music.get_pos() reports elapsed milliseconds.
            # The bar is a simple activity indicator because Pygame does not
            # provide the duration of a music stream.
            progress = (seconds % 60) / 60
            pygame.draw.rect(screen, (90, 180, 255),
                             (35, 250, int(620 * progress), 10), border_radius=5)

        controls = [
            "P  Play / Pause",
            "S  Stop",
            "N  Next track",
            "B  Previous track",
            "Q  Quit",
        ]
        for index, line in enumerate(controls):
            label = self.small_font.render(line, True, (235, 235, 235))
            screen.blit(label, (35 + (index % 3) * 210, 315 + (index // 3) * 35))
