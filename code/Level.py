from pygame import Surface, Rect 
from pygame.font import Font
import pygame
from code.Snake import Snake
from code.Food import Food
from code.Const import WIN_WIDTH, WIN_HEIGHT, HUD, C_GREEN, SNAKE_VELOCITY, PATH_BG_IMAGEM, BLOCK_SIZE, HUD, C_BLACK, FONT_SIZE_SCORE


class Level:
    def __init__(self, window: Surface):   
        self.window = window
        self.bg_imagem = pygame.image.load(PATH_BG_IMAGEM).convert_alpha() #carega a imagem
        self.background = pygame.transform.scale(self.bg_imagem, (WIN_WIDTH, WIN_HEIGHT))  # Ajusta a imagem ao tamanho da tela
        self.clock = pygame.time.Clock()    
        self.reset()
        self.score = 0
        self.best_score = 0

    def reset(self):
        self.snake = Snake()
        self.food = Food()

    def level_run(self):
        pygame.mixer_music.load('./assets/audio/level_sound.wav')
        pygame.mixer_music.play(-1) #'-1' faz a música tocar em loop infinito
        while True:
            self.events()
            self.to_update()
            self.draw()
            self.clock.tick(SNAKE_VELOCITY) # defini o fps do jogo

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP') 
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                    self.obj_sound('./assets/audio/direction.mp3')
                elif event.key  == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
                    self.obj_sound('./assets/audio/direction.mp3')
    
    def to_update (self):
        if self.snake.alive:
            self.snake.to_update_snake()
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]

            if x >= WIN_WIDTH:
                x = 0 
                
            elif x < 0:
                x = WIN_WIDTH - BLOCK_SIZE 

                
            elif y >= WIN_HEIGHT:
                y = HUD['hud_height']   
                
            elif y < HUD['hud_height']:
                y = WIN_HEIGHT - BLOCK_SIZE 
                

            x = (x // BLOCK_SIZE) * BLOCK_SIZE # '//' faz a divisão inteira garantido que o block_size seja sempre um número multiplo de 20
            y = (y // BLOCK_SIZE) * BLOCK_SIZE # Necessário para a cobra não perder o alinhamento com o grid, caso o contrário ele vai passar por cima da comida
            
            self.snake.body[0] = [x,y]

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                self.obj_sound('./assets/audio/eat.wav') # som da pontuação 
                self.score += 1
                self.food.relocate()
                self.snake.body.append(self.snake.body[-1])  # Cresce
        
        else:
            self.reset()

    def draw(self):
        self.window.blit(self.background, (0,0))
        self.hud(self.window)
        self.snake.draw_snake(self.window)
        self.food.draw_food(self.window)
        pygame.display.flip()

    def hud(self, window):
        #desenha retangulo que vai ser usado como hud
        pygame.draw.rect(window, C_GREEN, (HUD['hud_x'],HUD['hud_y'], HUD['hud_width'], HUD['hud_height']))

        center_y = (HUD['hud_height']/2) - (FONT_SIZE_SCORE / 2)
        margin_left = 20
        margin_top = 10
        margin_botton = 17
        self.level_text(FONT_SIZE_SCORE, f'Pontuação: {self.score} ', C_BLACK, (margin_left,center_y - margin_top))
        self.level_text(FONT_SIZE_SCORE, f'Melhor Pontuação: {self.best_score}', C_BLACK, (margin_left,center_y + margin_botton))



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        
    def obj_sound(self, path_sound):
        sound = pygame.mixer.Sound(path_sound)
        sound.play()
