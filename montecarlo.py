import random
import matplotlib.pyplot as plt
from memory_profiler import profile
import timeit

# Configuración
num_simulaciones = 100000  # Número de puntos a generar

@profile
def estimar_pi(num_simulaciones):
    puntos_dentro = 0
    puntos_x_dentro = []
    puntos_y_dentro = []
    puntos_x_fuera = []
    puntos_y_fuera = []

    # Generar puntos y contar cuántos caen dentro del círculo
    for _ in range(num_simulaciones):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            puntos_dentro += 1
            puntos_x_dentro.append(x)
            puntos_y_dentro.append(y)
        else:
            puntos_x_fuera.append(x)
            puntos_y_fuera.append(y)

    # Estimación de pi
    pi_estimado = 4 * (puntos_dentro / num_simulaciones)
    print(f"Valor estimado de pi: {pi_estimado}")

    # Visualización
    plt.figure(figsize=(8, 8))
    plt.scatter(puntos_x_dentro, puntos_y_dentro, color='blue', s=1, label='Dentro del círculo')
    plt.scatter(puntos_x_fuera, puntos_y_fuera, color='red', s=1, label='Fuera del círculo')

    # Dibujar el círculo
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    plt.gca().add_artist(circle)

    # Configuración del gráfico
    plt.title(f"Estimación de Pi usando Monte Carlo (Pi ≈ {pi_estimado:.4f})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.grid(True)

    plt.show()
    return pi_estimado

# Medir el tiempo de ejecución con timeit
def medir_tiempo():
    tiempo = timeit.timeit(lambda: estimar_pi(num_simulaciones), number=1)
    print(f"Tiempo de ejecución: {tiempo:.4f} segundos")

# Llamar a las funciones
if __name__ == "__main__":
    medir_tiempo()


#ANALISIS DE COMPLEJIDAD EMPÍRICA

#Resultados para n = 1000
"""

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     9     70.3 MiB     70.3 MiB           1   @profile
    10                                         def estimar_pi(num_simulaciones):
    11     70.3 MiB      0.0 MiB           1       puntos_dentro = 0
    12     70.3 MiB      0.0 MiB           1       puntos_x_dentro = []
    13     70.3 MiB      0.0 MiB           1       puntos_y_dentro = []
    14     70.3 MiB      0.0 MiB           1       puntos_x_fuera = []
    15     70.3 MiB      0.0 MiB           1       puntos_y_fuera = []
    16
    17                                             # Generar puntos y contar cuántos caen dentro del círculo   
    18     70.4 MiB  -5459.9 MiB       10001       for _ in range(num_simulaciones):
    19     70.4 MiB  -5459.7 MiB       10000           x = random.uniform(0, 1)
    20     70.4 MiB  -5459.1 MiB       10000           y = random.uniform(0, 1)
    21     70.4 MiB  -5459.4 MiB       10000           if x**2 + y**2 <= 1:
    22     70.4 MiB  -4240.1 MiB        7816               puntos_dentro += 1
    23     70.4 MiB  -4240.1 MiB        7816               puntos_x_dentro.append(x)
    24     70.4 MiB  -4240.4 MiB        7816               puntos_y_dentro.append(y)
    25                                                 else:
    26     70.4 MiB  -1219.5 MiB        2184               puntos_x_fuera.append(x)
    27     70.4 MiB  -1219.4 MiB        2184               puntos_y_fuera.append(y)
    28
    29                                             # Estimación de pi
    30     70.1 MiB     -0.3 MiB           1       pi_estimado = 4 * (puntos_dentro / num_simulaciones)        
    31     70.1 MiB      0.0 MiB           1       print(f"Valor estimado de pi: {pi_estimado}")
    32
    33                                             # Visualización
    34     88.2 MiB     18.1 MiB           1       plt.figure(figsize=(8, 8))
    35     89.8 MiB      1.6 MiB           1       plt.scatter(puntos_x_dentro, puntos_y_dentro, color='blue', s=1, label='Dentro del círculo')
    36     90.0 MiB      0.2 MiB           1       plt.scatter(puntos_x_fuera, puntos_y_fuera, color='red', s=1, label='Fuera del círculo')
    37
    38                                             # Dibujar el círculo
    39     90.0 MiB      0.0 MiB           1       circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    40     90.0 MiB      0.0 MiB           1       plt.gca().add_artist(circle)
    41
    42                                             # Configuración del gráfico
    43     90.0 MiB      0.0 MiB           1       plt.title(f"Estimación de Pi usando Monte Carlo (Pi ≈ {pi_estimado:.4f})")
    44     90.0 MiB      0.0 MiB           1       plt.xlabel("x")
    45     90.0 MiB      0.0 MiB           1       plt.ylabel("y")
    46     90.1 MiB      0.1 MiB           1       plt.legend()
    47     90.1 MiB      0.0 MiB           1       plt.axis('equal')
    48     90.1 MiB      0.0 MiB           1       plt.xlim(0, 1)
    49     90.1 MiB      0.0 MiB           1       plt.ylim(0, 1)
    50     90.1 MiB      0.0 MiB           1       plt.grid(True)
    51
    52     96.6 MiB      6.5 MiB           1       plt.show()
    53     96.6 MiB      0.0 MiB           1       return pi_estimado


Tiempo de ejecución: 10.3602 segundos"""

#   Resultados para  n= 100000