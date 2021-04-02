import pygame
from settings import Settings

settings = Settings()
sw = settings.screen_width
sh = settings.screen_height


class Button:  # 把鼠标移动上去的时候，它会将按钮缩小，移开后，又显示回原样。
    def __init__(self, upimage, downimage, position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.button_out = True

    def is_over(self):  # 判断鼠标是不是在这个按钮的上面
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()
        in_x = x - w / 2 < point_x < x + w / 2
        in_y = y - h / 2 < point_y < y + h / 2
        return in_x and in_y

    def render(self, screen):  # 判断显示哪张图
        w, h = self.imageUp.get_size()
        x, y = self.position
        x -= w / 2
        y -= h / 2
        if self.is_over():
            screen.blit(self.imageDown, (x + 2.5, y + 2.5))
            if self.button_out:
                self.button_out = False
        else:
            screen.blit(self.imageUp, (x, y))
            self.button_out = True


# 按钮子类
class ButtonsMain:  # 主界面按钮
    def __init__(self):
        self.buttons = [Button(".\\images\\kaishi.png", ".\\images\\kaishi.png", (320, 200)),
                        Button(".\\images\\3.png", ".\\images\\3_.png", (770, 670)),
                        Button(".\\images\\tuichu.png", ".\\images\\tuichu.png", (320, 350))]

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)


class ButtonFb:  # 游戏时按钮
    def __init__(self):
        self.buttons = [Button(".\\images\\5.png", ".\\images\\5_.png", (770, 80)),
                        Button(".\\images\\3.png", ".\\images\\3_.png", (770, 670)),
                        Button(".\\images\\1.png", ".\\images\\1_.png", (770, 30)),
                        Button(".\\images\\2.png", ".\\images\\2_.png", (770, 620))]

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)


class ButtonFb2:  # 暂停时按钮
    def __init__(self):
        self.buttons = [Button(".\\images\\5.png", ".\\images\\5_.png", (770, 80)),
                        Button(".\\images\\3.png", ".\\images\\3_.png", (770, 670)),
                        Button(".\\images\\4.png", ".\\images\\4_.png", (770, 30)),
                        Button(".\\images\\2.png", ".\\images\\2_.png", (770, 620))]

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)


class ButtonFb3:  # 死亡时按钮
    def __init__(self):
        self.buttons = [Button(".\\images\\5.png", ".\\images\\5_.png", (770, 80)),
                        Button(".\\images\\3.png", ".\\images\\3_.png", (770, 670)),
                        Button(".\\images\\4.png", ".\\images\\4_.png", (770, 30)),
                        Button(".\\images\\2.png", ".\\images\\2_.png", (770, 620)),
                        Button(".\\images\\5.png", ".\\images\\5_.png", (400, 300))]

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
