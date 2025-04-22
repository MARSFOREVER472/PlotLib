# DIAGRAMA DE LÍNEAS:

# Dibuja un polígono con los vértices dados por las coordenadas de la lista "x" en el eje X y las coordenadas de la lista "y" en el eje Y.

# PASO 1: IMPORTAREMOS LA LIBRERÍA "Matplotlib"...

import matplotlib.pyplot as plt

# PASO 2: CREAREMOS EL GRÁFICO CON RESPECTO AL EJE X...

fig, ax = plt.subplots()

# PASO 3: DIBUJAMOS LA GRÁFICA UNIENDO SOBRE LOS PUNTOS PARA FORMAR UNA LÍNEA...

ax.plot([1, 2, 3, 4], [1, 2, 0, 0.5])

# PASO 4: MOSTRAREMOS LA GRÁFICA...

plt.show()