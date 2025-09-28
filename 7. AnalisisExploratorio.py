

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
ataque = df.groupby('Tipo 1')['Ataque'].mean().round(1)
defensa = df.groupby('Tipo 1')['Defensa'].mean().round(1)

ataque_ordenado = ataque.sort_values(ascending=False)
defensa_ordenado = defensa.sort_values(ascending=False)

print("Ataque:", ataque_ordenado)
print("Defensa:", defensa_ordenado)
print("\n Con los calculos anteriores, se observa que en promedio los pokemons de tipo lucha tienen el mayor ataque, mientras que los de tipo roca tienen la mayor defensa")

#- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
correlacion = df["Ataque"].corr(df["Velocidad"]).round(1)
print("Correlacion entre ataque y velocidad :", correlacion)
print("\n La correlacion entre ataque y velocidad es baja, lo que nos muestra que no hay una relacion fuerte")

#- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
desviacion_por_tipo = df.groupby('Tipo 1')['PS'].std().round(1)
print("Desviacion estandar de PS por tipo :", desviacion_por_tipo)
print("\n Los tipo pokemon que tienen mayor numero en el indice de desviacion presentan una mayor diferencia de PS entre su propia categoria")

#- Identifica posibles outliers en los valores de ataque y PS usando boxplots.

df.boxplot(column="Ataque")
plt.title("Boxplot de Ataque")
plt.show()


df.boxplot(column="PS")
plt.title("Boxplot de PS")
plt.show()

