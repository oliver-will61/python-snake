from code.Data_json import Data_Json
from code.Const import DIFFICULTIES, SNAKE_VELOCITY


class Difficulty(Data_Json):
    def __init__(self):
        super().__init__()
        self.key_json = 'difficulty'
        self.selected = self.load_json(self.path_data_json, self.key_json)
        
        

    def apply_Difficulty(self):

        if self.selected ==  DIFFICULTIES[0]: #fácil
            snake_velocity = SNAKE_VELOCITY[DIFFICULTIES[0]]
            return snake_velocity

        elif self.selected ==  DIFFICULTIES[1]: #médio
            snake_velocity =  SNAKE_VELOCITY[DIFFICULTIES[1]]
            return snake_velocity

        elif self.selected == DIFFICULTIES[2]: #dificil
            snake_velocity =  SNAKE_VELOCITY[DIFFICULTIES[2]]
            return snake_velocity


