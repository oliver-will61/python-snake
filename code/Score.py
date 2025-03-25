import pygame
from pygame import Rect, Surface
from pygame.font import Font
from code.Const import C_GREEN, HUD, FONT_SIZE_SCORE, C_BLACK, FONT_SIZE_SCORE, PATH_DATA_JSON
from code.Data_json import Data_Json


class Score(Data_Json):
    def __init__(self):
        super().__init__()

        #self.path_json_data = './best_score.json'
        #self.best_score = self.load_best_score_json()
        self.best_score = self.load_json(PATH_DATA_JSON)
        self.current_score = 0
        
    def score_hud(self, window):
            self.window = window
            #desenha retangulo que vai ser usado como hud
            pygame.draw.rect(window, C_GREEN, (HUD['hud_x'],HUD['hud_y'], HUD['hud_width'], HUD['hud_height']))

            center_y = (HUD['hud_height']/2) - (FONT_SIZE_SCORE / 2)
            margin_left = 20
            margin_top = 10
            margin_botton = 17
            self.score_text(FONT_SIZE_SCORE, f'Pontuação: {self.current_score} ', C_BLACK, (margin_left,center_y - margin_top))
            self.score_text(FONT_SIZE_SCORE, f'Melhor Pontuação: {self.best_score['best_score']}', C_BLACK, (margin_left,center_y + margin_botton))

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    # def load_best_score_json(self):
    #     try:
    #         with open(f'{self.path_json_data}', 'r', encoding='utf-8') as file:
    #             data = json.load(file)
    #             return data
    #     except (FileNotFoundError, json.JSONDecodeError): 
    #         print('Erro ao carregar o arquivo JSON')

    # def update_best_score(self):
    #     if self.current_score > self.best_score['best_score']:
    #         try:
    #             with open(f'{self.path_json_data}', 'r', encoding='utf-8') as file:
    #                 data = json.load(file)
    #         except (FileNotFoundError, json.JSONDecodeError):
    #             print('Erro ao carregar o arquivo JSON')

    #         data['best_score'] = self.current_score

    #         with open(f'{self.path_json_data}', 'w', encoding='utf-8') as file:
    #             json.dump(data, file, indent=4) # Salva o JSON atualizado

