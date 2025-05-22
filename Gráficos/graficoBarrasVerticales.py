# DIAGRAMA DE BARRAS VERTICALES:
 
# bar(x, y): Dibuja un diagrama de barras verticales donde x es una lista con la posición de las barras en el eje X, e y es una lista con la altura de las barras en el eje Y.

# SOLUCIÓN:

# PASO 1: IMPORTAREMOS LA LIBRERÍA DE "Matplotlib":

import matplotlib.pyplot as plt

# PASO 2: CREAREMOS UNA GRÁFICA CON RESPECTO AL EJE X:

fig, ax = plt.subplots()

# PASO 3: DIBUJAREMOS LA GRÁFICA DE BARRAS EN POSICIÓN VERTICAL (HACIA ARRIBA):

ax.bar([1, 2, 3], [3, 2, 1])

# PASO 4: MOSTRAREMOS LA GRÁFICA COMPLETA:

plt.show()