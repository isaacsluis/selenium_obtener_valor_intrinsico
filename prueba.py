
listado_company = ['MSFT','BRK.B']

from datetime import datetime

def archivo(nombre_imagen,company,valor_accion,valor_intrinsico):

    
    archivo = open(f'C://Users//Isaacs//Documents//Obsidian//Cerebro Digital//Cerebro Digital//200 Mis Intereses//Trading//Analisis Stock//{company}.md', 'a')

    archivo.write(f'\n*{company}* Fecha {datetime.now().date()}\n![[{nombre_imagen}]] \n Valor Accion *{valor_accion}* -- Valor Intrinsico *{valor_intrinsico}*')

    archivo.close


archivo('MSFT-2023-12-26.png','Microsoft Corp','374.66','354.77')