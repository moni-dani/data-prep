import pandas as pd

def main():
    try:
        # Ruta correcta al archivo
        file_path = "data/conjunto_de_datos_ensu_2025_2t_csv/conjunto_de_datos_ensu_cb_0625/conjunto_de_datos/conjunto_de_datos_ensu_cb_0625.csv"
        
        print(f"📂 Cargando archivo...")
        raw_data = pd.read_csv(file_path)
        
        # Filtrar datos de Yucatán
        yucatan_data = raw_data[raw_data["NOM_ENT"] == "YUCATÁN"]
        
        # Si no encuentra con acento, probar sin acento
        if yucatan_data.empty:
            yucatan_data = raw_data[raw_data["NOM_ENT"] == "YUCATAN"]
        
        # Imprimir el resultado que quieres
        print(yucatan_data.shape)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()