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
import shutil
from datetime import datetime

## para manipular los datos del html
from bs4 import BeautifulSoup

#listado_company = ['MSFT','BRK.B']
listado_company = ['MSFT','BRK.B','GOOGL','AAPL','KO','F','V','MA','AXP']

def cambiar_ubicacion_y_nombre(ticket,nombre_company,valor_accion,valor_intrinsico):
    # Construir la ruta original y la nueva ruta
    ruta_original = os.path.abspath('C:/Users/Isaacs/Documents/Curso Blockchain/Python/scraping/prueba/chart.png')
    #nueva_ruta = os.path.join(os.path.abspath('C:/Users/Isaacs/Downloads'), f"{tiquet}+{datetime.now()}+'.png'")
    nombre_imagen = ticket+'-'+str(datetime.now().date())+'.png'
    print(nombre_imagen)
    nueva_ruta = os.path.join(os.path.abspath(r'C:\Users\Isaacs\Documents\Obsidian\Cerebro Digital\Cerebro Digital\200 Mis Intereses\Trading\Analisis Stock\ANEXOS'), nombre_imagen)

    try:
        # Mover el archivo a la nueva ubicación
        shutil.move(ruta_original,nueva_ruta)
        print(f"Archivo movido exitosamente a: {'C:/Users/Isaacs/Documents/Curso Blockchain/Python/scraping/'}")
        archivo(nombre_imagen,nombre_company,valor_accion,valor_intrinsico)
        print('archivo escrito')
    except FileNotFoundError:
        print(f"El archivo no se encuentra en la ubicación original: {'C:/Users/Isaacs/Documents/Curso Blockchain/Python/scraping/prueba/chart.png'}")
    except Exception as e:
        print(f"Error al mover el archivo: ")



def boot():
    ## se genera esta ruta para que este disponible el navegador
    ruta = ChromeDriverManager().install()

    # Configurar las opciones de Chrome para manejar las descargas
    options = Options()
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Isaacs\Documents\Curso Blockchain\Python\scraping\prueba",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })
    service = Service(ruta)

    # Crear una instancia del navegador Chrome con las opciones configuradas
    driver = webdriver.Chrome(service=service,options=options)
    return driver

def navegation(driver, ticket, url):
    # Navegar a la página que contiene el botón de descarga
    driver.get(url)
    
    time.sleep(10)
    
    # Localizar el botón que inicia la descarga y hacer clic en él
    wait = WebDriverWait(driver,10)
    elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/section/main/div[1]/div[4]/div[2]/div[2]/div[1]/div[2]/div/span/div/span')))
    elemento.click()
    elemento = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/ul/li[1]/span')))
    elemento.click()

    # funcion que captura los datos
    soap_datos(driver,ticket)
    

def soap_datos(driver,ticket):
    ### Funcion que se encarga de convertir todo el html en soup y de este tomar los datos necesarios

    ## convierte el html y lo convierte en parser html
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    ## trae el nombre y el precio de la acion
    nombre_company = soup.find('h1', class_='t-h5').text
    print(nombre_company)
    ## tiene una logica de lipiador replace remplaza el los valores y strip() quita espacion y enters
     
    valor_accion = soup.find('span', class_='bold t-body-lg').text.replace('$', "").strip()
    print(valor_accion)
    # trae el valor intrinsico
    valor_intrinsico = soup.find_all('span', class_='t-primary')[2].text.replace('$', "").strip()
    print(valor_intrinsico)

    time.sleep(10)  
    cambiar_ubicacion_y_nombre(ticket,nombre_company,valor_accion,valor_intrinsico)
    time.sleep(10)
    

def archivo(nombre_imagen,nombre_company,valor_accion,valor_intrinsico):

    
    archivo = open(f'C://Users//Isaacs//Documents//Obsidian//Cerebro Digital//Cerebro Digital//200 Mis Intereses//Trading//Analisis Stock//{nombre_company}.md', 'a')

    archivo.write(f'\n*{nombre_company}* Fecha {datetime.now().date()}\n![[{nombre_imagen}]] \n Valor Accion *{valor_accion}* -- Valor Intrinseco *{valor_intrinsico}*')

    archivo.close

def principal():
    driver = boot()
    for ticket in listado_company:
        print(ticket)
        navegation(driver, ticket, url=f"https://www.gurufocus.com/stock/{ticket}/summary")
        
        
    driver.quit()
    #input('Enter')
    


principal()