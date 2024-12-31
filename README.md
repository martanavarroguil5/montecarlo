# montecarlo
Este código consiste en una implementación de un caso real del algoritmo de Montecarlo. Básicamente estimamos el valor del número pi a partir de la generación de puntos que van a caer dentro y fuera de un círuclo inscrito en un cuadrado.


Sencillamente se introduce el número de simulaciones, es decir el número de puntos que se van a genrar, y se veririfica si esos puntos pertenencen a un círculo de radio 1 (puede ser el que se apero se necesita  ajustar al lado del cuadrdo). Esto se verifica de la siguiente manera: x^2 + y^2 = 1. Con los resultados obtenidos hacemos una proporcion entre los puntos que caen en el círculo y los puntos que no para obtener una estimación del número pi.



A su vez, para hacerlo mas visual, en una grafica con matplotlib se proyectan todos los puntos recogidos y se dibuja el circulo. si caen dentro se dibuja azul sino rojo.


También se encuentra el análisis empírico de la complejidad temporal y espacial.
