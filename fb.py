import pygame
import sys
from settings import Settings
import button
import musics
import main
from functions import return_game, createMap, checkDead, getResutl, pause, write_score
from classes import Ball, Enemy


settings = Settings()


class Game:
    def __init__(self):
        """初始化游戏"""
        pygame.init()  # 创建一个屏幕对象
        self.screen = pygame.display.set_mode((800, 700))  # 设置屏幕显示
        self.font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 450)
        self.buttonfb = button.ButtonFb()
        self.enemy_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.ball = Ball()
        self.ball_group.add(self.ball)

    def run_game(self):
        while True:
            self.clock.tick(60)
            # 监视键盘和鼠标
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write_score()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttonfb.buttons[0].is_over():     # 重新开始
                        write_score()
                        settings.score = 0
                        settings.speed = 450
                        play()
                    elif self.buttonfb.buttons[1].is_over():   # 音乐按钮
                        musics.pause_music()
                    elif self.buttonfb.buttons[2].is_over():   # 暂停游戏
                        pause(self)
                    elif self.buttonfb.buttons[3].is_over():   # 返回主界面
                        write_score()
                        settings.score = 0
                        settings.speed = 450
                        main.play()
                    else:
                        settings.jump_active = True  # 跳跃
                        self.ball.down_speed = 5  # 重力
                        self.ball.up_speed = 10  # 跳跃高度
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause(self)
                    elif event.key == pygame.K_r:
                        write_score()
                        settings.score = 0
                        settings.speed = 450
                        play()
                if event.type == pygame.KEYDOWN and not self.ball.dead:
                    if event.key == pygame.K_SPACE:
                        settings.jump_active = True      # 跳跃
                        self.ball.down_speed = 5         # 重力
                        self.ball.up_speed = 10          # 跳跃高度
                if event.type == pygame.USEREVENT:   # 创建障碍物
                    if settings.score % 20 == 0 and settings.score < 250:   # 控制障碍物生成速度
                        settings.speed -= 20
                    pygame.time.set_timer(pygame.USEREVENT, settings.speed)
                    enemy = Enemy()  # 将障碍物添加到障碍物组
                    self.enemy_group.add(enemy)
            if checkDead(self):  # 检测球生命状态
                getResutl(self)  # 如果球死亡，显示游戏总分数
                musics.death_music()  # 死亡音效
                return_game(self)  # 显示重新开始游戏
            else:
                createMap(self)  # 更新地图
            # 让最近绘制的屏幕可见
            pygame.display.flip()


def play():
    game = Game()
    game.run_game()
