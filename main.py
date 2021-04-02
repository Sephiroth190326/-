import pygame
import sys
from settings import Settings
import button
import fb
import musics


class Main:
    def __init__(self):
        """初始化游戏"""
        pygame.init()  # 创建一个屏幕对象
        self.settings = Settings()  # 开始时游戏的设置
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 设置屏幕显示
        pygame.display.set_caption("墨风云")  # 设置窗口名
        pygame.display.set_icon(self.settings.tubiao)  # 设置窗口图标

    def run_game(self):
        # 设置主界面按钮
        buttons = button.ButtonsMain()
        # 开始游戏的主循环
        while True:
            # 监视键盘和鼠标
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if buttons.buttons[0].is_over() and not self.settings.game_active:  # 开始游戏
                        fb.play()
                    elif buttons.buttons[1].is_over() and not self.settings.game_active:  # 音乐按钮
                        musics.pause_music()
                    elif buttons.buttons[2].is_over() and not self.settings.game_active:  # 退出游戏
                        pygame.quit()
                        sys.exit()
            # 播放主界面音乐
            musics.play_music_main()
            # 每次循环时重绘屏幕
            self.screen.blit(self.settings.background_main, (0, 0))
            buttons.render(self.screen)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


def play():
    game = Main()
    game.run_game()


# 开始游戏
if __name__ == '__main__':
    play()
