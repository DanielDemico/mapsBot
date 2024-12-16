import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pegarEnd import dataframes
import numpy as np

lock = threading.Lock()

#Selenium
def process_enderecos(dataframe):
    navegador = webdriver.Chrome()
    action = ActionChains(navegador)
    navegador.get("https://www.google.com.br/maps/@-21.9570078,-50.5032108,15z?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D")

    
    while True:
        try:
            tela = navegador.find_element(By.XPATH, '//canvas[contains(@class,"aFsglc widget-scene-canvas") and (@tabindex="-1")]')
            break
        except:
            sleep(1)
            action.move_by_offset(100, 200).click().perform()

    digitar_endereco = navegador.find_element(By.XPATH, '//input[contains(@class,"fontBodyMedium searchboxinput xiQnY")]')

    local_resultados = []  

    for linha in dataframe.apply(lambda x: f"{x['Street']} {x['Neighborhood']} {x['City']} {x['State']} {x['ZIP Code']}", axis=1):
        digitar_endereco.clear()
        sleep(0.5)
        digitar_endereco.send_keys(linha)
        sleep(0.5)
        digitar_endereco.send_keys(Keys.ENTER)
        sleep(0.5)
        action.move_to_element_with_offset(tela, 100, 100).context_click().perform()
        sleep(0.5)
        
        while True:
            try:
                coordenadas = navegador.find_element(By.XPATH, '//div[contains(@class,"fxNQSd") and @data-index="0"]//div[contains(@class,"twHv4e")]//div[contains(@class,"mLuXec")]').text
                break
            except:
                continue
        
        local_resultados.append(coordenadas)
        
        print("valor adicionado:", coordenadas)
        sleep(0.5)

    with lock:
        resultados_compartilhados.extend(local_resultados)
        
    navegador.quit()
    

resultados_compartilhados = []


threads = []

#Threading 
for dataframe in dataframes:
    t = threading.Thread(target=process_enderecos, args=(dataframe,))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


print("Resultados finais:", resultados_compartilhados)
print(len(resultados_compartilhados))