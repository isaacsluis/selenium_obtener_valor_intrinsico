
'''
### crea archivos
nuevo_archivo = open('nombrearchivo.txt', 'w')

### escribe sobre el archvio
nuevo_archivo.write('Prueba')

### cierra el archivo
nuevo_archivo.close

### abre el archivo en mode de escribir una linea al final
nuevo_archivo = open('nombrearchivo.txt', 'a')

nuevo_archivo.write('\n![[Pasted image 20231024092852.png]]')

nuevo_archivo.close


#### abre el archivo en modo lectura
nuevo_archivo = open('nombrearchivo.txt', 'r')

print(nuevo_archivo.read())

nuevo_archivo.close()

'''



def archivo():

    archivo = open(r'C:\Users\Isaacs\Documents\Obsidian\Cerebro Digital\Cerebro Digital\200 Mis Intereses\Trading\Analisis Stock\nombrearchivo.md', 'a')

    archivo.write('\n![[Pasted image 20231024092852.png]] nueva ruta')

    archivo.close

archivo()