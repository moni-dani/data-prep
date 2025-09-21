import pandas as pd

# Define la ruta al archivo de resultados que quieres ver.
# Puedes cambiar este nombre de archivo para ver datos de otro trimestre.
file_path = "processed_data/yucatan_insecurity_conjunto_de_datos_ensu_cb_0625.csv"

# Lee el archivo CSV en un DataFrame de pandas
df_resultados = pd.read_csv(file_path)

# Imprime el DataFrame para mostrarlo como una tabla en la terminal
print(df_resultados)