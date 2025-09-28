#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.


import pandas as pd 
from Verificador import verificar_csv
csv = 'pokemon_primera_gen.csv'

#Verificacion de datos
errores = verificar_csv(csv)
if errores:
    print("Errores encontrados en los datos")
    for e in errores:
        print("-",e)
    raise SystemExit(1)
else:
    print("No se encontraron errores en los datos")


df = pd.read_csv('pokemon_primera_gen.csv')

filtro_fuego = df[df["Tipo 1"] == "Fuego"]

df_filtrado = filtro_fuego[["Nombre", "Tipo 1", "Ataque", "Velocidad"]]

print(df_filtrado)