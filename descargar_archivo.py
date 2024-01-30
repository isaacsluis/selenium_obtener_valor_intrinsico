## para controlar los tiempos
from selenium.webdriver.support.ui import WebDriverWait ## para definir por elementos en selenium
from selenium.webdriver.support import expected_conditions as ec ## para condiciones en selenimo

#para definir el tiepo de busqueda del elemento
from selenium.webdriver.common.by import By

# para instalar automaticamente chomedriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

## librerias sugeridas por chatgpt
from selenium import webdriver
import os
import time

## se genera esta ruta para que este disponible el navegador
ruta = ChromeDriverManager().install()

# Configurar las opciones de Chrome para manejar las descargas

options = Options()
options.add_argument('--start-maximized')


options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Isaacs\Documents\Curso Blockchain\Python\scraping",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

#options.add_experimental_option()

service = Service(ruta)

# Crear una instancia del navegador Chrome con las opciones configuradas

driver = webdriver.Chrome(service=service,options=options)

# Navegar a la página que contiene el botón de descarga
driver.get("https://www.gurufocus.com/stock/F/summary")

# Localizar el botón que inicia la descarga y hacer clic en él
wait = WebDriverWait(driver,10)
elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/section/main/div[1]/div[4]/div[2]/div[2]/div[1]/div[2]/div/span/div/span')))
elemento.click()
elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/ul/li[1]/span')))
elemento.click()

# Esperar hasta que el archivo se descargue completamente (ajusta según sea necesario)
time.sleep(10)


# Cerrar el navegador
input('Enter para terminar')
driver.quit()
