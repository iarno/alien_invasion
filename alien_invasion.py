"""
👽 外星人入侵
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.secren_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # 开始游戏主循环
    while True:
        # 监听鼠标键盘事件
        gf.check_events(ship)

        # 移动飞船
        ship.update()

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship)

run_game()
