"""
设置窗口相关属性值
"""

class Settings():
    """所有设置类"""

    def __init__(self) -> None:
        """初始化游戏设置"""

        self.screen_width = 1200
        self.secren_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
