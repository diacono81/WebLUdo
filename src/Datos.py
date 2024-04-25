import openpyxl
from tabulate import tabulate

# Cargar el libro de trabajo de Excel
excel_workbook = openpyxl.load_workbook("Datos.xlsm")

# Obtener la hoja 2 del libro de trabajo
hoja2 = excel_workbook["Codigo"]  # Reemplaza "Nombre_de_la_hoja_2" con el nombre real de la hoja 2

# Convertir los datos de la hoja a una lista de listas
datos_lista = []
for fila in hoja2.iter_rows(values_only=True):
    datos_lista.append(fila)

# Imprimir los datos en formato tabular usando tabulate
print(tabulate(datos_lista, headers="firstrow"))

