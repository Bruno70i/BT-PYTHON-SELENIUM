# BOT PYTHON SELENIUM

from selenium import webdriver
import time


# definir navegador
navegador = webdriver.Chrome()



# definir um site
navegador.get('https://www.instagram.com/?hl=pt-br')

time.sleep(5)