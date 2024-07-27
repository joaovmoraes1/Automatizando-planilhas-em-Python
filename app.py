from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

# 1 - Entrar no site - https://precos-de-produtos.netlify.app/
driver = webdriver.Chrome()
driver.get('https://precos-de-produtos.netlify.app/')
sleep(5)
# 2.1 - rolar a página inteira para baixo para carregar os produtos 
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# 2.2 - clicar em "carregar mais" para visualizar o restante dos produtos
botao_carregar_mais = driver.find_element(By.XPATH,"//button[@id='loadMoreButton']")
sleep(2)
botao_carregar_mais.click()
sleep(2)
# 3 - Rolar a página totalmente para baixo
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

# 4 - Subir totalmente de volta para o topo
driver.execute_script('window.scrollTo(0,0);')
sleep(2)

# 5 - Clicar em Subir planilha de preços
botao_carregar_planilha_de_produtos = driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-custom']")
sleep(2)
botao_carregar_planilha_de_produtos.click()
sleep(5)

# 6 - Carregar planilha "preços-produtos-atualizados.xlsx"
pyautogui.write(r'C:\automacao\precos-produtos-atualizados.xlsx')
sleep(2)
pyautogui.press('enter')
input('Aperte enter no terminal para fechar o programa')