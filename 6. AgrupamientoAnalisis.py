

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

#- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
ataque = df.groupby('Tipo 1')['Ataque'].agg(['mean', 'median', 'std'])
print(ataque)

#- ¿Qué tipo tiene el mayor promedio de velocidad?
velocidad = df.groupby('Tipo 1')['Velocidad'].mean().round(1)
mayor_velocidad = velocidad.idxmax()
promedio_velocidad = velocidad.max()
print(mayor_velocidad, promedio_velocidad)

#- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
ps_max = df.loc[df.groupby('Tipo 1')['PS'].idxmax(), ['Tipo 1', 'Nombre', 'PS']]
ps_min = df.loc[df.groupby('Tipo 1')['PS'].idxmin(), ['Tipo 1', 'Nombre', 'PS']]

print(ps_max)
print(ps_min)