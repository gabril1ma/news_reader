from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

programa = os.path.dirname(sys.executable)  # colocando o diretorio que o executavel vai ser criado

hoje = datetime.now()  # variavel para pegar a data que foi executado
data = hoje.strftime("%d%m%Y")  # formatando a data em dia mes e ano

site = "https://www.cnnbrasil.com.br/"  # variavel com o link do site que vai ser analisado
path = "D:/downloads/chromedriver/chromedriver.exe"  # o diretorio onde o chromedriver esta


options = Options()  # criando a variavel options para a função options
options.headless = True  # ativando o modo headless que faz com que o site a ser analisado não abra em primeiro plano

driver_service = Service(executable_path=path)  # variavel para executar o chrome driver
driver = webdriver.Chrome(service=driver_service, options=options)  # ativar tbm o chromedriver e o options
driver.get(site)  # o driver pega a variavel onde está armazenado o link do site

noticia = driver.find_elements(by="xpath", value='//section[@id="block216160"]/ul/li')  # o codigo xpath pra ser analisado

# titulos = []
textos = []  # lista para pegar os dados da noticia
links = []  # lista para armazenar os links das noticias


for news in noticia:  # estrutura de repetição para pegar todos os dados que estejam dentro do xpath

    texto = news.find_element(by="xpath", value='./a').text  # o diretorio xpath e o que queremos dele no caso texto
    link = news.find_element(by="xpath", value='./a').get_attribute("href")  # mesma coisa do de cima mas pegando agr o link(href)

    textos.append(texto)  # colocando a noticia encontrada dentro da lista de textos das noticias
    links.append(link)  # colocando os links dentro da lista


meu_dicionario = {"noticia": textos,  # dicionario colocando os textos e links com a chave
                  "link": links}

file_name = f"noticias de {data}.csv"  # o nome do arquivo que ira ser criado depois de executar o .exe
final_path = os.path.join(programa, file_name)  # definindo o path final onde ele vai pegar a variavel do os e do nome

dic_dataframe = pd.DataFrame(meu_dicionario)  # colocando o dicionario no dataframe
dic_dataframe.to_csv(final_path)  # e transferindo os dados para um arquivo csv

driver.quit()  # aqui pra quando terminar de realizar as funções ele sair do programa



