
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

df = pd.read_csv('pokemon_primera_gen.csv')


#- Haz un histograma de los valores de ataque.
plt.hist(df["Ataque"], bins=5, color='blue')
plt.title('Histograma de Ataque')
plt.xlabel('Ataque')
plt.ylabel('Frecuencia')
plt.show()


#- Realiza un gráfico de dispersión entre ataque y velocidad.
plt.scatter(df["Ataque"], df["Velocidad"], color='green')
plt.title('Gráfico de Dispersión: Ataque vs Velocidad')
plt.xlabel('Ataque')
plt.ylabel('Velocidad')
plt.show()

#- Haz un boxplot de los PS por tipo principal (Tipo 1).
df.boxplot(column='PS', by='Tipo 1', figsize=(8, 5))
plt.title('Boxplot de PS por Tipo 1') 
plt.xlabel('Tipo 1')
plt.ylabel('PS')
plt.show()

#- Grafica la distribución de la defensa usando un diagrama de violín.
sns.violinplot(y='Defensa', data=df)
plt.title('Grafico de Violín de Defensa')
plt.ylabel('Defensa')
plt.show()

