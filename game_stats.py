class GameStats():
    def __init__(self, pa_settings):
        self.pa_settings = pa_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.pachimari_left = self.pa_settings.pachimari_limit