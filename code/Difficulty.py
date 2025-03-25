from code.Data_json import Data_Json
from code.Const import DIFFICULTIES


class Difficulty(Data_Json):
    def __init__(self):
        super().__init__()
        self.selected = ''
        self.key_json = 'difficulty'
        
        print(self.selected)

    def apply_Difficulty(self, snake_velocity):


        if self.difficulty.selected ==  DIFFICULTIES[0]: #fácil
            snake_velocity = 5

        elif self.difficulty.selected ==  DIFFICULTIES[1]: #médio
            snake_velocity = 10

        elif self.difficulty.selected == DIFFICULTIES[2]: #dificil
            snake_velocity = 20


