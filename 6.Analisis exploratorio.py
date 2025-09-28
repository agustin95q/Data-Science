#7. Análisis exploratorio (EDA)
    # - ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
    # - ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
    # - ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
    # - Identifica posibles outliers en los valores de ataque y PS usando boxplots.
    
import pandas as pd
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


csv = "pokemon_primera_gen.csv"
df_pokemon = pd.read_csv(csv)


#Calculo del promedio de ataque y defensa por tipo de pokemon
ataque_defensa = df_pokemon.groupby("Tipo 1")[["Ataque", "Defensa"]].mean().round(1)

#Ordenamiento de los tipos con mayor ataque y defensa en promedio
mas_ataque = ataque_defensa.sort_values("Ataque", ascending=False ).head()
mas_defensa = ataque_defensa.sort_values("Defensa", ascending=False ).head()

#Calculo del coeficiente de correlacion entre ataque y velocidad
correlacion_ataque_velocidad = df_pokemon["Ataque"].corr(df_pokemon["Velocidad"])
correlacion_ataque_velocidad = round(correlacion_ataque_velocidad, 2)

#Calculo de desviacion estandar de los PS por tipo de pokemon
desviacion_ps = df_pokemon.groupby("Tipo 1")["PS"].std().round(1)


#Muestra de la desviacion estandar por tipo
print("\nTABLA DE DESVIACION ESTANDAR DE LOS PS POR CADA TIPO")
print(desviacion_ps)
print("\n||Los tipo de pokemon con un numero mayor en el indice de desviacion estandar presentan una mayor diferencia de PS entre su propia categoria de pokemon's||")

