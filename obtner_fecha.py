from datetime import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Imprimir la fecha actual
print("Fecha actual:", fecha_actual)


print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Obtener solo la fecha
fecha = fecha_actual.date()

# Imprimir la fecha
print("Fecha actual:", fecha)

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')


# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Formatear la fecha como una cadena con un formato específico
fecha_formateada = fecha_actual.strftime("%d-%Y-%m")

# Imprimir la fecha formateada
print("Fecha actual formateada:", fecha_formateada)
