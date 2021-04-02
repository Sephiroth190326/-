import pygame


class Settings:
    """游戏设置"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800     # 窗口宽度
        self.screen_height = 700    # 窗口高度
        self.music_active = True    # 音乐播放控制
        self.game_active = False    # 游戏活动控制
        self.jump_active = False    # 球跳跃控制
        self.score = 0              # 得分
        self.speed = 450            # 障碍物生成速度
        self.background_main = pygame.image.load(".\\images\\main.jpg")   # 主界面背景
        self.background_fb = pygame.image.load(".\\images\\beijing.jpg")  # 游戏背景
        self.tubiao = pygame.image.load(".\\images\\tubiao.ico")  # 窗口图标
