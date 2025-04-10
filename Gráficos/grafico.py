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