import pandas as pd

# Ruta del archivo original
archivo_original = 'Google-Playstore.csv'

# Ruta del archivo de salida (sample)
archivo_sample = 'Google-Playstore-mini.csv'

# Leer el CSV original (ajusta el delimitador si no es coma)
df = pd.read_csv(archivo_original)

# Tomar solo las primeras 20 filas
df_sample = df.head(20)

# Guardar el nuevo CSV
df_sample.to_csv(archivo_sample, index=False)

print(f"Archivo de muestra guardado como: {archivo_sample}")
