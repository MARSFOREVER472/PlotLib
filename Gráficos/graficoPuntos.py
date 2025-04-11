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