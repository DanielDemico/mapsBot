import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pegarEnd import dataframes
import numpy as np

lock = threading.Lock()
lats = []
lngs  = []
navegador = webdriver.Chrome()
navegador.get("https://www.mapsdirections.info/pt/coordenadas-gps.html")


for df in dataframes:
    for i in df.apply(lambda x: f"{x['Street']}, {x['Neighborhood']}, {x['City']}, {x['State']}", axis=1 ):
            input_adress = navegador.find_element(By.XPATH,'//input[contains(@id,"street_address")]')
            input_adress.send_keys(i)
            time.sleep(1)
            input_adress.send_keys(Keys.ENTER)
            time.sleep(5)

            
            sem_resultados = navegador.find_element(By.XPATH,'//div[contains(@id,"results")]').text
            
            if sem_resultados == "Não encontrado":
                lats.append(np.NaN)
                lngs.append(np.NAN)
                print("NAN")
                navegador.execute_script('arguments[0].value = "";', input_adress)
                continue
            
            primeira_opcao = navegador.find_element(By.XPATH,'//div[contains(@role,"option")][1]')
            primeira_opcao.click()
            time.sleep(1)
            lat = navegador.find_element(By.XPATH,'//input[contains(@id,"marker-lat")]').get_attribute('value')
            print("Pegamos a latitude")
            print(lat)
            time.sleep(1)
        
       
            lng = navegador.find_element(By.XPATH,'//input[contains(@id,"marker-lng")]').get_attribute('value')
            print("Pegamos a longitude")
            print(lng)
            time.sleep(1)

           
            lats.append(lat)
            lngs.append(lng)
            navegador.execute_script('arguments[0].value = "";', input_adress)
    
