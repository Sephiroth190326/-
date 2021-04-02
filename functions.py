import pygame
import sys
import button
import musics
import main
import fb


def createMap(self):
    """定义创建地图的方法"""
    self.screen.blit(fb.settings.background_fb, (0, 0))  # 填入到背景
    # 显示障碍物
    self.enemy_group.update()
    self.enemy_group.draw(self.screen)
    # 显示球
    self.ball_group.update()       # 球移动
    self.ball_group.draw(self.screen)         # 设置球的坐标
    # 显示分数与按钮
    with open('Topscore.txt') as file_object:
        contents = file_object.read()
    self.screen.blit(self.font.render('Score:' + str(fb.settings.score), -1, (0, 0, 0)), (150, 0))  # 设置颜色及坐标位置
    self.screen.blit(self.font.render('Top score:' + contents, -1, (0, 0, 0)), (400, 0))
    self.buttonfb.render(self.screen)
    pygame.display.flip()    # 更新显示


def checkDead(self):
    if not 0 < self.ball.rect.y < fb.settings.screen_height or \
            pygame.sprite.spritecollide(self.ball, self.enemy_group, False, pygame.sprite.collide_circle):
        self.ball.dead = True
        return True
    else:
        return False


def getResutl(self):
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(fb.settings.score)
    pygame.font.SysFont("Arial", 70)
    ft1_surf = self.font.render(final_text1, 1, (242, 3, 36))                        # 设置第一行文字颜色
    pygame.font.SysFont("Arial", 50)
    ft2_surf = self.font.render(final_text2, 1, (253, 177, 6))                       # 设置第二行文字颜色
    self.screen.blit(ft1_surf, [self.screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    self.screen.blit(ft2_surf, [self.screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pygame.display.update()                                                          # 更新整个待显示的Surface对象到屏幕上


def pause(self):
    buttonfb2 = button.ButtonFb2()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 重新开始
                if buttonfb2.buttons[0].is_over():
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    fb.play()
                elif buttonfb2.buttons[1].is_over():  # 音乐按钮
                    musics.pause_music()
                elif buttonfb2.buttons[2].is_over():  # 继续游戏
                    paused = False
                    pygame.time.wait(500)
                elif self.buttonfb.buttons[3].is_over():  # 返回主界面
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    main.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # 继续游戏
                    paused = False
                    pygame.time.wait(500)
                elif event.key == pygame.K_r:  # 重新开始
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    fb.play()
        buttonfb2.render(self.screen)
        pygame.display.update()  # 更新显示


def return_game(self):
    buttonfb3 = button.ButtonFb3()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonfb3.buttons[0].is_over() or buttonfb3.buttons[2].is_over() or buttonfb3.buttons[4].is_over():
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    fb.play()  # 开始游戏
                elif buttonfb3.buttons[1].is_over():  # 音乐按钮
                    musics.pause_music()
                elif self.buttonfb.buttons[3].is_over():  # 返回主界面
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    main.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_r:  # 开始游戏
                    write_score()
                    fb.settings.score = 0
                    fb.settings.speed = 450
                    fb.play()
        buttonfb3.render(self.screen)
        pygame.display.update()  # 更新显示


def write_score():        # 比较分数，写入最高分
    with open('Topscore.txt') as file_object:
        contents = file_object.read()
    if int(contents) < fb.settings.score:
        with open('Topscore.txt', 'w') as file_object:
            file_object.write(str(fb.settings.score))
