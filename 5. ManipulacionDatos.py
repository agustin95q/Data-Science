
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.

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

df["Poder Total"] = df["Ataque"] + df["Defensa"] + df["Velocidad"] + df["PS"]

df_ordenado = df.sort_values(by="Poder Total", ascending=False)
print(df_ordenado)