import pandas as pd


file_path = "processed_data/yucatan_insecurity_conjunto_de_datos_ensu_cb_0625.csv"

df_resultados = pd.read_csv(file_path)

# DataFrame 
print(df_resultados)