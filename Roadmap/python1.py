import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# Cargar el dataset de Spotify y limpiar nombres de columnas
df = pd.read_csv("spotifydataset.csv")
df.columns = df.columns.str.strip()  # Eliminar espacios en los nombres de columna

# Seleccionar las 10 canciones más populares
df_sorted = df.sort_values(by="track_popularity", ascending=False).head(10)

# Crear la carpeta `docs/` si no existe
os.makedirs("docs", exist_ok=True)

# Guardar los datos en un archivo JSON
json_data = df_sorted.to_json(orient="records", indent=4)

with open("docs/datos_spotify.json", "w") as json_file:
    json_file.write(json_data)

print("✅ Archivo JSON generado exitosamente: docs/datos_spotify.json")

# Mejorar el diseño del gráfico
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
colores = sns.color_palette("coolwarm", len(df_sorted))  # Colores vibrantes

plt.barh(df_sorted["track_name"], df_sorted["track_popularity"], color=colores, edgecolor="black")

# Ajustes de diseño
plt.xlabel("Popularidad", fontsize=12, fontweight="bold")
plt.ylabel("Canción", fontsize=12, fontweight="bold")
plt.title("🎶 Top 10 Canciones por Popularidad en Spotify 🎶", fontsize=14, fontweight="bold")
plt.gca().invert_yaxis()  # Invertir el orden para mejor lectura

# Guardar el gráfico correctamente en la carpeta `docs/`
plt.savefig("docs/grafico_spotify.png", dpi=300, bbox_inches="tight")

print("✅ Gráfico guardado correctamente en docs/grafico_spotify.png")

plt.show()
