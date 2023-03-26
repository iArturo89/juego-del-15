import copy

class Node:
    def __init__(self, estado_inicial, padre, costo):
        self.estado_inicial = estado_inicial
        self.padre = padre
        self.costo = costo
    
    def get_sucesor(self):
        # Obtener las coordenadas de la casilla vacía
        pos_vacia = None
        for i in range(3):
            for j in range(3):
                if self.estado_inicial[i][j] == 0:
                    pos_vacia = (i, j)
                    break
        
        # Generar los sucesores del estado actual
        sucesor = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            i, j = pos_vacia[0] + dy, pos_vacia[1] + dx
            if 0 <= i < 3 and 0 <= j < 3:
                # Intercambiar la casilla vacía con la adyacente
                new_estado_inicial = copy.deepcopy(self.estado_inicial)
                new_estado_inicial[pos_vacia[0]][pos_vacia[1]] = new_estado_inicial[i][j]
                new_estado_inicial[i][j] = 0
                
                # Crear un nuevo nodo sucesor y agregarlo a la lista de sucesores
                sucesor.append(Node(new_estado_inicial, self, self.costo + 1))
        return sucesor

    def get_ruta(self):
        # Obtener el camino desde la raíz hasta este nodo
        ruta = []
        node = self
        while node is not None:
            ruta.append(node)
            node = node.padre
        return list(reversed(ruta))

def h(estado_inicial):
    # Calcular la heurística para el estado actual
    # En este caso, se utiliza la distancia Manhattan
    # entre cada casilla y su posición final
    h_valor = 0
    for i in range(3):
        for j in range(3):
            if estado_inicial[i][j] != 0:
                x, y = divmod(estado_inicial[i][j] - 1, 3)
                h_valor += abs(i - x) + abs(j - y)
    return h_valor

def ida_star(raiz):
    limite_superior = h(raiz.estado_inicial)
    ruta = [raiz]
    while True:
        siguiente_limite = buscar(ruta, 0, limite_superior)
        if siguiente_limite  == 0:
            return ruta
        if siguiente_limite  == float('inf'):
            return None
        limite_superior = siguiente_limite 

def buscar(ruta, g, limite_superior):
    node = ruta[-1]
    siguiente_limite  = g + h(node.estado_inicial)
    if siguiente_limite  > limite_superior:
        return siguiente_limite 
    if node.estado_inicial == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return 0
    min_costo = float('inf')
    for successor in node.get_sucesor():
        if successor not in ruta:
            ruta.append(successor)
            siguiente_limite  = buscar(ruta, g + 1, limite_superior)
            if siguiente_limite  == 0:
                return 0
            if siguiente_limite  < min_costo:
                min_costo = siguiente_limite 
            ruta.pop()
    return min_costo

def jugar():
    # Crear el estado inicial del juego
    estado_inicial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # Mezclar el estado inicial para comenzar el juego
    import random
    for i in range(1000):
        sucesor = Node(estado_inicial, None, 0).get_sucesor()
        estado_inicial = random.choice(sucesor).estado_inicial
    
    # Crear el nodo raíz del árbol de búsqueda
    raiz = Node(estado_inicial, None, 0)
    
    # Resolver el juego utilizando el algoritmo IDA*
    solucion = ida_star(raiz)
    
    # Mostrar la solución
    if solucion is None:
        print("No se encontró una solución.")
    else:
        for i, node in enumerate(solucion):
            print(f"Paso {i}:")
            for row in node.estado_inicial:
                print(row)
            print()

jugar()
