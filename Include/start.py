# para instalar automaticamente chomedriver
from webdriver_manager.chrome import ChromeDriverManager
# driver de selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#para modificar las opciones de wecrevier en Chrome
from selenium.webdriver.chrome.options import Options

# operaciones relacionadas con el sistema de archivos, directorios y otros aspectos del sistema operativo. 
import os

def star_program(descargas=None):
    '''
    Inicia el programa para escrapiar y descargar los archivos
    '''
    ## se genera esta ruta para que este disponible el navegador
    ruta = ChromeDriverManager().install()

    ###instancia creada para eliminar el texto de la consola
    options = Options()
    options.add_argument('--start-maximized')
    exp_opt = [
            'enable-automation',
            'ignore-certificate-errors',
            'enable-logging'
        ]
    options.add_experimental_option('excludeSwitches',exp_opt)

    service = Service(ruta)

    driver = webdriver.Chrome(service=service,options=options)

    ## llama la funcion que se encarga de la ruta de descarga
    dir_descargas(driver,descargas)

    return driver


def dir_descargas(driver, ruta):


    ### Gestiona la descarga del archivo seleccionado -- ruta es la carpeta qeu se genera 
    

    driver.command_executor._commands['send_chrome_command'] = ['POST','/session/$sessionId/chromium/send_command']
    params = {
        'cmd':'Page.setDownloadBehavior',
        'params': {
            'behavior':'allow',
            'downloadPath': os.path.abspath(ruta)
        }
    }
    driver.execute('send_chrome_command',params) 
