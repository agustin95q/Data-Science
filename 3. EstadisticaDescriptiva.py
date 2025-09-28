
#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).

import pandas as pd 
import numpy as np
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

#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
promedio = df["Ataque"].mean().round(1)
mediana = df["Ataque"].median().round(1)
moda = df["Ataque"].mode().round(1)

print("Promedio ataque :", promedio, "Mediana ataque :", mediana, "Moda ataque :", moda)


#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
indice_max = df["Defensa"].idxmax()
indice_min = df["Velocidad"].idxmin()

defensa_max = df.loc[indice_max, ["Nombre", "Defensa"]]
menor_velocidad = df.loc[indice_min, ["Nombre", "Velocidad"]]

print(" Mayor defensa :", defensa_max, "Menor velocidad :", menor_velocidad)

#- ¿Cuántos Pokémon tienen dos tipos?

Contador_tipos = df["Tipo 2"].count()
print("Pokemon con dos tipos :", Contador_tipos)

#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).

rango = df["PS"].max() - df["PS"].min()
desviacion_estandar = df["PS"].std().round(1)

print("Rango :", rango, "Desviacion estandar  :", desviacion_estandar)