import pygame
from settings import Settings

settings = Settings()


def play_music_main():
    """主音乐"""
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(".\\music\\backgroud.mp3")
        pygame.mixer.music.play(-1)  # 无限循环


def pause_music():     # 暂停音乐
    if settings.music_active:
        pygame.mixer.music.pause()
        settings.music_active = False
    else:
        pygame.mixer.music.unpause()
        settings.music_active = True


def death_music():        # 死亡音效
    death = pygame.mixer.Sound(".\\music\\death.wav")
    death.play()
