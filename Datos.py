import pandas as pd

# Leer el archivo de Excel
df = pd.read_excel('datos.xlsx')

# Generar el HTML de la tabla
html_table = df.to_html(index=False)

# Imprimir el HTML
print(html_table)
