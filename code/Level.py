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
                elif event.key  == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key  == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key  == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
    
    def to_update (self):
        if self.snake.alive:
            self.snake.to_update_snake()
            
            # verifica colisão com a parede
            x, y = self.snake.body[0]
            print(x, y)

            if x >= WIN_WIDTH:
                print(f'X maior ou igual a 1160 - X:{x}')
                x = 0 # O -20 do block serve para compesar a andada da cobra
                print(f'Valor de X agora é: {x}')
                
            elif x < 0:
                print(f'X menor que 0 - X:{x}')
                x = WIN_WIDTH - BLOCK_SIZE 
                print(f'Valor de X agora é: {x}')

                
            elif y >= WIN_HEIGHT:
                print(f'Y maior ou igual a 660 - Y:{y}')
                y = HUD['hud_height']   # O -20 do block serve para compesar a andada da cobra
                print(f'Valor de Y agora é: {y}')
                
            elif y < HUD['hud_height']:
                print(f'Y menor que 0 - Y :{y}')
                y = WIN_HEIGHT - BLOCK_SIZE 
                print(f'Valor de Y agora é: {y}')
                

            x = (x // BLOCK_SIZE) * BLOCK_SIZE # '//' faz a divisão inteira garantido que o block_size seja sempre um número multiplo de 20
            y = (y // BLOCK_SIZE) * BLOCK_SIZE # Necessário para a cobra não perder o alinhamento com o grid, caso o contrário ele vai passar por cima da comida
            
            self.snake.body[0] = [x,y]

            #verifica se comeu a comida

            if self.snake.body[0] == self.food.position:
                eat_sound = pygame.mixer.Sound('./assets/audio/eat.wav')
                eat_sound.play()
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
        self.level_text(FONT_SIZE_SCORE, f'Pontuação: {self.score}', C_BLACK, (20,(HUD['hud_height']/2)-(FONT_SIZE_SCORE/2)))



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        