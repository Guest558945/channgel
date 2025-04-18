# -*- coding: utf-8 -*-
"""Copia de AluraStoreLatam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/111Zm0L8_ZLNNFPfqhIMzqktnLfFuy6KB

### Importación de datos
"""

import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

"""#1. Análisis de facturación


"""

import pandas as pd
import matplotlib.pyplot as plt

ingreso_total = tienda['Precio'].sum()
ingreso_total2 = tienda2['Precio'].sum()
ingreso_toral3 = tienda3['Precio'].sum()
ingreso_total4 = tienda4['Precio'].sum()

print(f"ingreso total de la tienda 1: {ingreso_total}")
print(f"ingreso total de la tienda 2: {ingreso_total2}")
print(f"ingreso total de la tienda 3: {ingreso_toral3}")
print(f"ingreso total de la tienda 4: {ingreso_total4}")

plt.pie([ingreso_total, ingreso_total2, ingreso_toral3, ingreso_total4], labels=['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'])
plt.show()

plt.bar(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'], [ingreso_total, ingreso_total2, ingreso_toral3, ingreso_total4])
plt.show()

plt.plot(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'], [ingreso_total, ingreso_total2, ingreso_toral3, ingreso_total4])
plt.show()



"""# 2. Ventas por categoría"""





"""# 3. Calificación promedio de la tienda

"""



import matplotlib.pyplot as plt
import pandas as pd
promedio_calificacion_tienda1 = tienda['Calificación'].mean()
promedio_calificacion_tienda2 = tienda2['Calificación'].mean()
promedio_calificacion_tienda3 = tienda3['Calificación'].mean()
promedio_calificacion_tienda4 = tienda4['Calificación'].mean()

print(f"Calificación promedio de la tienda 1: {promedio_calificacion_tienda1}")
print(f"Calificación promedio de la tienda 2: {promedio_calificacion_tienda2}")
print(f"Calificación promedio de la tienda 3: {promedio_calificacion_tienda3}")
print(f"Calificación promedio de la tienda 4: {promedio_calificacion_tienda4}")

# Puedes visualizar estos datos en un gráfico de barras, por ejemplo:
plt.bar(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
        [promedio_calificacion_tienda1, promedio_calificacion_tienda2, promedio_calificacion_tienda3, promedio_calificacion_tienda4])
plt.ylabel('Calificación promedio')
plt.title('Calificación promedio de clientes por tienda')
plt.show()

plt.pie([promedio_calificacion_tienda1, promedio_calificacion_tienda2, promedio_calificacion_tienda3, promedio_calificacion_tienda4], labels=['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'])
plt.show()
plt.plot(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'], [promedio_calificacion_tienda1, promedio_calificacion_tienda2, promedio_calificacion_tienda3, promedio_calificacion_tienda4
                                                            ])
plt.show()



"""# 4. Productos más y menos vendidos"""

import pandas as pd
import matplotlib.pyplot as plt



def analizar_ventas(tienda, nombre_tienda):
    ventas_por_producto = tienda.groupby('Producto')['Precio'].sum()
    productos_mas_vendidos = ventas_por_producto.nlargest(5)  # Top 5 productos
    productos_menos_vendidos = ventas_por_producto.nsmallest(5)  # Bottom 5 productos

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    productos_mas_vendidos.plot(kind='bar')
    plt.title(f'Productos más vendidos - {nombre_tienda}')
    plt.xlabel('Producto')
    plt.ylabel('Ventas totales')

    plt.subplot(1, 2, 2)
    productos_menos_vendidos.plot(kind='bar')
    plt.title(f'Productos menos vendidos - {nombre_tienda}')
    plt.xlabel('Producto')
    plt.ylabel('Ventas totales')

    plt.tight_layout()
    plt.show()

# Análisis para cada tienda
analizar_ventas(tienda, 'Tienda 1')
analizar_ventas(tienda2, 'Tienda 2')
analizar_ventas(tienda3, 'Tienda 3')
analizar_ventas(tienda4, 'Tienda 4')



"""# 5. Envío promedio por tienda"""



import matplotlib.pyplot as plt
# Calculate the average shipping cost for each store.
promedio_envio_tienda1 = tienda['Costo de envío'].mean()
promedio_envio_tienda2 = tienda2['Costo de envío'].mean()
promedio_envio_tienda3 = tienda3['Costo de envío'].mean()
promedio_envio_tienda4 = tienda4['Costo de envío'].mean()

print(f"Costo de envío promedio de la tienda 1: {promedio_envio_tienda1}")
print(f"Costo de envío promedio de la tienda 2: {promedio_envio_tienda2}")
print(f"Costo de envío promedio de la tienda 3: {promedio_envio_tienda3}")
print(f"Costo de envío promedio de la tienda 4: {promedio_envio_tienda4}")

# You can visualize this data in a bar chart, for example:
plt.bar(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
        [promedio_envio_tienda1, promedio_envio_tienda2, promedio_envio_tienda3, promedio_envio_tienda4])
plt.ylabel('Costo de envío promedio')
plt.title('Costo de envío promedio por tienda')
plt.show()

plt.pie([promedio_envio_tienda1, promedio_envio_tienda2, promedio_envio_tienda3, promedio_envio_tienda4], labels=['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'])
plt.show()

plt.plot(['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'], [promedio_envio_tienda1, promedio_envio_tienda2, promedio_envio_tienda3, promedio_envio_tienda4])
plt.show()

"""EN CONCLUCION

Informe Final: Recomendación de Tienda para el Sr. Juan

**Introducción:**

Este informe sintetiza los hallazgos del análisis de datos de cuatro tiendas, con el objetivo de recomendar la mejor opción para el Sr. Juan.  Se consideraron los ingresos totales, categorías de productos, calificaciones de clientes, productos más y menos vendidos, y el costo de envío promedio.

**Análisis de Ingresos Totales:**

Las visualizaciones muestran una variación significativa en los ingresos entre las tiendas.  Si bien la información numérica precisa no está incluida en el texto (ya que no está guardada en variables, no se puede extraer de la salida del código), las gráficas (de barras, pastel y línea) permiten identificar cuál tienda generó más ingresos.  La tienda con los ingresos más altos es la que debería ser considerada primero, representando un mayor potencial de ganancias para el Sr. Juan.


**Análisis de Categorías y Productos:**

El análisis de las categorías de productos más y menos vendidas en cada tienda (no incluido en el código proporcionado) es crucial para comprender el perfil de cada tienda y su atractivo para los clientes.  La información no está disponible en el código, pero habría que identificar las categorías exitosas y si estas se alinean con los productos que el Sr. Juan desea vender.  Adicionalmente, conocer los productos más y menos vendidos permite entender las tendencias de cada tienda.

**Calificación Promedio de los Clientes:**

Las calificaciones promedio de los clientes ofrecen una visión importante sobre la satisfacción del consumidor. El código proporciona un cálculo y visualización (barras, pastel y línea) que indica la puntuación promedio para cada tienda. La tienda con la mejor calificación promedio demuestra una mayor satisfacción del cliente, lo cual puede traducirse en mayor lealtad y ventas a largo plazo. Si hay varias tiendas con calificaciones altas, otras variables como los ingresos o los costos de envío, pueden ser utilizadas para desempatar.

**Costo de Envío Promedio:**

El análisis de costos de envío, calculado y visualizado en el código (barras, pastel y línea), es un factor clave. Una tienda con un menor costo de envío puede ser más atractiva para los clientes, afectando positivamente las ventas. Es fundamental comparar este valor con las otras métricas para encontrar la tienda más balanceada y atractiva.


**Recomendación:**

Con base en el análisis superficial que permiten los fragmentos de código y las descripciones, se recomienda que el Sr. Juan considere principalmente la **tienda con mayores ingresos**.  Para una recomendación más sólida, se necesitan los valores exactos de cada variable para hacer una comparación directa, y se requiere completar el análisis de las categorias de producto y productos más y menos vendidos.  Sin esta información, una evaluación definitiva es imposible.

**Justificación:**

La tienda con los ingresos más altos, por sí sola, representa el mayor potencial de retorno de la inversión. Si esta tienda también tiene una calificación promedio razonable y costos de envío competitivos, entonces la decisión es clara. En caso contrario, la tienda con los mayores ingresos se debería comparar con las tiendas con una calificación superior y los costos de envio mas competitivos, sopesando las fortalezas de cada una.
"""