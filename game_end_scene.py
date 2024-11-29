from levels import Scene
from text_box import TextBox
from button import Button
from globals import SCREEN_W,SCREEN_H

class GameOverScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen, scene_manager)
        self.game_over_box = TextBox(screen,SCREEN_W//2,SCREEN_H*0.2,'Game Over',font_size=50)
        self.score_text_box = TextBox(screen,SCREEN_W//2,SCREEN_H*0.32,'Score',)
        self.score_text_value = TextBox(screen,SCREEN_W//2,SCREEN_H*0.4,'',dynamic_text='mined_resources')
        self.main_menu_button = Button(screen,SCREEN_W//2,SCREEN_H//2,action='set_main_menu')

        self.elements = [
            self.game_over_box,
            self.score_text_box,
            self.score_text_value,
            self.main_menu_button,
        ]
    
    def draw(self):
        super().draw()
        for element in self.elements:
            element.draw()


class GameWonScene(Scene):
    def __init__(self, screen, scene_manager):
        super().__init__(screen, scene_manager)
        self.game_won_box = TextBox(screen,SCREEN_W//2,SCREEN_H*0.2,'Game Won',font_size=50)
        self.score_text_box = TextBox(screen,SCREEN_W//2,SCREEN_H*0.32,'Score',)
        self.score_text_value = TextBox(screen,SCREEN_W//2,SCREEN_H*0.4,'',dynamic_text='mined_resources')
        self.main_menu_button = Button(screen,SCREEN_W//2,SCREEN_H//2,action='set_main_menu')
        self.thanks_for_playing_box = TextBox(screen,SCREEN_W//2,SCREEN_H*0.7,'Thanks for playing!',font_size=40)

        self.elements = [
            self.score_text_box,
            self.score_text_value,
            self.main_menu_button,
            self.thanks_for_playing_box
        ]
    
    def draw(self):
        super().draw()
        for element in self.elements:
            element.draw()