# @Author : dcg

class Settings:
    """设置类"""

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        # 背景颜色
        self.bg_color = (230, 230, 230)

        '飞船设置'
        self.ship_limit = 4  # 定义生命数量
        self.ship_speed = 1.5  # 定义飞船移动速度

        '子弹设置'
        self.bullet_speed = 1  # 定义子弹的速度
        self.bullet_allowed = 10  # 定义允许发射的子弹数量
        self.bullet_width = 3  # 子弹宽
        self.bullet_height = 15  # 子弹高
        self.bullet_color = (60, 60, 60)  # 子弹颜色

        '外星人设置'
        self.alien_x_speed = 1  # 定义外星人移动速度
        self.alien_y_speed = 30  # 定义外星人移动速度
        self.fleet_direction = 1  # 定义外星人移动方向

        '游戏节奏'
        self.speedup_scale = 1.1  # 定义游戏速度提升的比例
        self.score_scale = 1.5  # 定义游戏分数提升的比例
        self.initialize_dynamic_settings()  # 初始化游戏节奏

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_x_speed = 1.0

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_x_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)