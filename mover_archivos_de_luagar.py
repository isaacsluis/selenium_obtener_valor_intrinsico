import shutil
import os

def cambiar_ubicacion_y_nombre(ubicacion_original, nuevo_directorio, nuevo_nombre):
    # Construir la ruta original y la nueva ruta
    ruta_original = os.path.abspath(ubicacion_original)
    nueva_ruta = os.path.join(os.path.abspath(nuevo_directorio), nuevo_nombre)

    try:
        # Mover el archivo a la nueva ubicación
        shutil.move(ruta_original, nueva_ruta)
        print(f"Archivo movido exitosamente a: {nueva_ruta}")
    except FileNotFoundError:
        print(f"El archivo no se encuentra en la ubicación original: {ubicacion_original}")
    except Exception as e:
        print(f"Error al mover el archivo: {str(e)}")

# Ejemplo de uso
ubicacion_archivo_descargado = 'C:/Users/Isaacs/Documents/Curso Blockchain/Python/scraping/BRK.B/chart.png'
nuevo_directorio = 'C:/Users/Isaacs/Downloads'
nuevo_nombre_archivo = 'nuevo_nombre.png'

cambiar_ubicacion_y_nombre(ubicacion_archivo_descargado, nuevo_directorio, nuevo_nombre_archivo)

