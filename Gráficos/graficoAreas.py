# DIAGRAMA DE AREAS:

# fill_between(x, y): Dibuja el area bajo el polígono con los vértices dados por las coordenadas de la lista x en el eje X y las coordenadas de la lista y en el eje Y.

# PASO 1: IMPORTAMOS LA LIBRERÍA ESTÁNDAR DE PYTHON EN VISUAL STUDIO CODE:

import matplotlib.pyplot as plt

# PASO 2: CREAMOS LA GRÁFICA MEDIANTE INTERVALOS:

fig, ax = plt.subplots()

# PASO 3: DIBUJAMOS EL GRÁFICO DE ÁREAS:

ax.fill_between([1, 2, 3, 4], [1, 2, 0, 0.5])

# PASO 4: MOSTRAMOS LA GRÁFICA:

plt.show() 