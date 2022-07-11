"""
添加飞船图像
"""
import pygame

from settings import Settings

class Ship():
    """飞船"""
    def __init__(self, ai_settings:Settings, screen:pygame.Surface) -> None:
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.ship_rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """将图像绘制到屏幕"""
        self.screen.blit(self.image, self.ship_rect)

    def update(self):
        """移动飞船✈️"""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.ship_rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.ship_rect.centerx = self.center
            
        