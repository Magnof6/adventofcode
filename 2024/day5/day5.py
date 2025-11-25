from collections import defaultdict, deque

orden = "orden.txt"
update = "update.txt"
def procesar_orden(archivo_orden, archivo_update):
    with open(archivo_orden,  'r') as orden_file:
        reglas = [tuple(map(int, line.strip().split('|'))) for line in orden_file if line.strip()]
    with open(archivo_update, 'r') as update_file:
        actualizaciones = [
            list(map(int, line.strip().split(','))) for line in update_file if line.strip()
        ]
    def es_correcta(update, reglas):
        for x, y in reglas:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
        return True
    ##
    # La función es_correcta verifica si una
    # actualización cumple con las reglas dadas.
    
    def ordenar_incorrectas(pages, reglas):
        #Construimos el grafo con las páginas presentes
        grafo = defaultdict(list) #Creamos un diccionario de listas para representar el grafo
        in_degree = {p: 0 for p in pages} #Contamos cuantas páginas apuntan a cada página
        for x, y in reglas:
            if x in pages and y in pages: #Solo consideramos las reglas que involucran páginas presentes
                grafo[x].append(y) #Linea de x a y
                in_degree[y] += 1 #aumentamos el grado de entrada de y ya que tiene una nueva conexión entrante desde x
        ##
        # Para ordenar las páginas incorrectas, utilizamos el algoritmo de Kahn
        # Se usa para ordenar topologicamente grafos dirigidos acíclicos, no se repiten
        # Si A -> B, A siempre aparecerá antes que B#
        cola = deque([p for p in pages if in_degree[p] == 0]) #Todas las paginas sin predecesores van primero
        ordenado = []
        while cola: #Mientras haya nodos sin predecesores
            nodo = cola.popleft() #Sacamos el primero de la cola (FIFO)
            ordenado.append(nodo) #Lo añadimos a la lista ordenada
            for vecino in grafo[nodo]: #Revisamos sus vecinos, vecinos son los nodos que no pueden ir antes que el nodo actual
                in_degree[vecino] -= 1 #Como hemos colocado nodo en ordenado , reducimos el grado de entrada de sus vecinos
                if in_degree[vecino] == 0: #Si algun vecino ya no tiene predecesores
                    cola.append(vecino) #Lo añadimos a la cola para procesarlo
        return ordenado
        
        
        
        
    suma_medios = 0
    for upd in actualizaciones:
        if not es_correcta(upd, reglas):
            corregida = ordenar_incorrectas(upd, reglas)
            medio = corregida[len(corregida)//2] # // Devuelve la parte entera de la división
            suma_medios += medio
    return suma_medios
    

print("La suma de los elementos medios es:", procesar_orden(orden, update))