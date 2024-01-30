from selenium.webdriver.chrome.service import Service
#para modificar las opciones de wecrevier en Chrome

## para controlar los tiempos
from selenium.webdriver.support.ui import WebDriverWait ## para definir por elementos en selenium
from selenium.webdriver.support import expected_conditions as ec ## para condiciones en selenimo

#para definir el tiepo de busqueda del elemento
from selenium.webdriver.common.by import By

## para detener un tiempo prudente
import time

from start import star_program

listado_company = ['MSFT','BRK.B','GOOGL']
#listado_company = ['MSFT','BRK.B','GOOGL','AAPL','KO','F','V','MA','AXP']


def buscar_archivo_descarga(driver):
    '''
    Busca el elemto y le da click 2 veces para seleccionar y despues descargar el la imagen de la grafica
    '''
    wait = WebDriverWait(driver,10)
    elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/section/main/div[1]/div[4]/div[2]/div[2]/div[1]/div[2]/div/span/div/span')))
    elemento.click()
    elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/ul/li[1]/span')))
    elemento.click()


def generacion_imagenes():
    '''
    recorre la lista y descarga las imagenes de cada company
    '''
    for i in listado_company:
        driver = star_program(i)
        driver.get(f'https://www.gurufocus.com/stock/{i}/summary')
        buscar_archivo_descarga(driver)
        time.sleep(4)
    #return driver
    input('Pulse Enter para terminar')

if __name__ == '__main__':

    driver = generacion_imagenes()
    
    

    

