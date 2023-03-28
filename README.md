# juego-del-15
usando el algoritmo IDA*. para el juego del 15 en un tamaño de 3x3 con fichas numeradas, 
con una ficha faltante que puede moverse por la cuadrícula. El objetivo del rompecabezas es llegar a la configuración final de las fichas

Clase Node
Representa un nodo en el árbol de búsqueda. Cada nodo contiene lo siguiente:

estado_inicial: el estado del rompecabezas representado como una lista 2D
padre: el nodo padre
costo: el costo de llegar a este nodo desde el estado inicial
La clase Node también tiene 
get_sucesor(): genera todos los posibles sucesores del estado actual y los devuelve como una lista de objetos Node.
