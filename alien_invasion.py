"""
👽 外星人入侵
"""

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.secren_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监听鼠标键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 移动飞船
        ship.update()

        bullets.update()

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
