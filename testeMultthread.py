from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import threading

def pesquisarPalavra(palavra):
    navegador = webdriver.Chrome()
    navegador.get("https://www.google.com")
    
    campo_de_pesquisa = navegador.find_element(By.XPATH,'//*[@id="APjFqb"]')
    campo_de_pesquisa.send_keys(palavra)
    campo_de_pesquisa.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    print(f"Título para {palavra} {navegador.title}")
    
    navegador.quit()
    
palavras = ["python","Selenium","banana"]

threads = []

for palavra in palavras:
    t = threading.Thread(target=pesquisarPalavra,args=(palavra,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print("todas as pesquisas foram concluidas")