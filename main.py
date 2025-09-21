import pandas as pd
import os

def process_ensu_data(input_file_path, output_dir):
    """
    Procesa un solo archivo de datos ENSU para calcular las percepciones de inseguridad
    en Yucatán y guarda el resultado en un archivo CSV.
    """
    try:
        raw_data = pd.read_csv(input_file_path)

        # Filtra los datos para el estado de Yucatán
        yucatan_data = raw_data[raw_data["NOM_ENT"] == "YUCATAN"]

        # Selecciona las columnas relevantes
        yucatan_filtered = yucatan_data[["NOM_ENT", "NOM_MUN", "NOM_CD", "BP1_1"]]

        # Agrupa, cuenta y calcula los totales de percepción
        grouped = yucatan_filtered.groupby(["NOM_ENT", "NOM_MUN", "NOM_CD"]).agg(
            TOTAL_REGISTROS=("BP1_1", "count"),
            TOTAL_SEGUROS=("BP1_1", lambda x: (x == 1).sum()),
            TOTAL_INSEGUROS=("BP1_1", lambda x: (x == 2).sum()),
            TOTAL_NO_RESPONDE=("BP1_1", lambda x: (x == 9).sum())
        ).reset_index()

        # Calcula los porcentajes
        grouped["PORCENTAJE_SEGUROS"] = (grouped["TOTAL_SEGUROS"] / grouped["TOTAL_REGISTROS"]).round(2) * 100
        grouped["PORCENTAJE_INSEGUROS"] = (grouped["TOTAL_INSEGUROS"] / grouped["TOTAL_REGISTROS"]).round(2) * 100
        grouped["PORCENTAJE_NO_RESPONDE"] = (grouped["TOTAL_NO_RESPONDE"] / grouped["TOTAL_REGISTROS"]).round(2) * 100

        # Crea un nombre de archivo de salida basado en el archivo de entrada
        file_name = os.path.basename(input_file_path)
        output_file_name = f"yucatan_insecurity_{file_name}"
        output_file_path = os.path.join(output_dir, output_file_name)

        # Guarda el resultado en un nuevo CSV
        grouped.to_csv(output_file_path, index=False)
        print(f"✅ Procesado y guardado: {output_file_path}")

    except FileNotFoundError:
        print(f"❌ Error: El archivo {input_file_path} no fue encontrado.")
    except Exception as e:
        print(f"❌ Error procesando {input_file_path}: {e}")

def main():
    # Define la ruta del directorio que contiene tus datos
    data_dir = "data"

    # Define la ruta para los resultados procesados
    output_dir = "processed_data"

    # Crea el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Recorre todos los subdirectorios para encontrar los archivos CSV
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            # Revisa si el archivo es un CSV de datos ENSU
            if file.startswith("conjunto_de_datos_ensu_cb_") and file.endswith(".csv"):
                full_path = os.path.join(root, file)
                print(f"🔍 Encontrado archivo: {full_path}")
                process_ensu_data(full_path, output_dir)

if __name__ == "__main__":
    main()