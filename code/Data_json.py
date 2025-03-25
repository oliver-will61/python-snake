import json

class Data_Json:
    def __init__(self):
        pass
    


    def load_json(self, path):
        try:
            with open(f'{path}', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError): 
            print('Erro ao carregar o arquivo json_data')

    def update_json(self, path:str, key:str, value):

        try:
            with open(f'{path}', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print('Erro ao carregar o arquivo JSON')

        data[key] = value

        try:
            #Escreve o json atualizado no arquivo
            with open(f'{path}', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4) # Salva o JSON atualizado

        except Exception as e:
            print(f'Erro ao salvar o JSON: {e}')