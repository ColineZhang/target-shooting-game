class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (245, 245, 245)

        self.ship_speed = 6
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (80, 60, 60)
        self.bullets_allowed = 100


        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.super_mode = False

    def initialize_dynamic_settings(self):

        self.bullet_speed = 3
        self.alien_speed = 0.25
        self.fleet_drop_speed = 5

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)

    def widen_bullet(self):
        self.bullet_width *= 2
