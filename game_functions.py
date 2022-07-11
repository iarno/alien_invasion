"""
事件
"""

import sys
import pygame
from pygame.event import Event
from settings import Settings
from ship import Ship

def check_keydown_events(event:Event, ship:Ship):
    """键盘按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """键盘松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship:Ship):
    """监听按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings:Settings, screen:pygame.Surface, ship:Ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
