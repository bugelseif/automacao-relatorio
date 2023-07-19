# Import for the Files Plugin
from botcity.plugins.files import BotFilesPlugin

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Outras bibliotecas
from pandas import DataFrame
from datetime import datetime

def main():

    # instancia do plugin
    bot = BotFilesPlugin()

    # busca pelos arquivos em um diretório retornando uma lista
    caminho = r"...\Notas"  # exemplo --> C:\Users\Bugs\Desktop\Notas
    lista = bot.get_all_file_paths(caminho)

    # retira o caminho e a extensão de cada arquivo e
    # adiciona o nome em uma nova lista
    lista_notas = []
    for arquivo in lista:
        nome_arquivo = arquivo.strip(fr"{caminho}.txt")
        lista_notas.append(nome_arquivo)
    

    # define um caminho e nome para o arquivo .csv
    hoje = datetime.today().strftime("%d-%m-%Y")
    # exemplo --> C:\Users\Bugs\Desktop\relatorio\notas{hoje}.csv
    caminho_relatorio = fr"...\relatorio\notas{hoje}.csv"
    
    # converte a lista de nomes em .csv e
    # salva no caminho definido
    data_frame = DataFrame(lista_notas)
    data_frame.to_csv(caminho_relatorio)

    print("### Finalizou ###")


if __name__ == '__main__':
    main()
