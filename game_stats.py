import json
class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        with open('/Users/kexuanzhang/Desktop/PythonLearning/alien_invasion/high_score.json') as file_object:
            self.high_score = json.load(file_object)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def store_high_score(self):
        with open('/Users/kexuanzhang/Desktop/PythonLearning/alien_invasion/high_score.json', 'w') as file_object:
            json.dump(self.high_score, file_object)
