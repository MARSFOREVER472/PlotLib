# IMPORTAMOS GRÁFICAS BÁSICAS DESDE UN MÓDULO DENOMINADO "pyplot" JUNTO CON EL ALIAS "plt"...

import matplotlib.pyplot as plt

# CREAREMOS LA FIGURA Y LOS EJES...

fig, ax = plt.subplots()

# DIBUJAMOS LOS PUNTOS DE LA GRÁFICA...

ax.scatter(x = [1, 2, 3], y = [3, 2, 1])

# GUARDAR LA GRÁFICA EN FORMATO .png...

plt.savefig("Diagrama_Dispersion.png")

# MOSTRAR LA GRÁFICA SEÑALADA...

plt.show()

# DIAGRAMAS DE DISPERSIÓN O DE PUNTOS...

# scatter(x, y): Dibuja un diagrama de puntos con las coordenadas de la lista x en el eje X y las coordenadas de la lista y en el eje Y. 

# IMPORTAREMOS COMO SIEMPRE LA LIBRERÍA "Matplotlib"...

import matplotlib.pyplot as plt

# CREACIÓN DE EJES Y FIGURAS...

fig, ax = plt.subplots()

# DIBUJAMOS LA GRÁFICA SEÑALADA...

ax.scatter([1, 2, 3, 4], [1, 2, 0, 0.5])

# MUESTRA LA GRÁFICA...

plt.show()