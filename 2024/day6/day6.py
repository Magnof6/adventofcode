from collections import deque #deque se usa para crear una cola eficiente
mapa = "map.txt"

def simular_patrulla(map_lines):
    """
    map_lines: es una lista de strings(cada string es una fila del mapa)
    devuelve (n_visitadas, mapa con x ) devuelve el numero de cassilas
    que ha visitado y el mapa con las x donde ha pasado la patrulla
    """
    grid = [list(line.rstrip('\n')) for line in map_lines]
    rows = len(grid)
    cols = len(grid[0])
    
    # Encontrar la posición inicial y dirección
    dirs = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
        } #{'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    
    start = None #inicializamos la variable sin darle valor
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dirs:
                if start is not None:
                    raise ValueError("Hay más de una posición inicial de la patrulla.")
                start = (r, c)
                dr, dc = dirs[grid[r][c]]
                
                break
        if start:
            break
    if start is None:
        raise ValueError("No se encontró la posición inicial de la patrulla.")
    visited = set() #conjunto para almacenar las posiciones visitadas
    
    r, c = start
    visited.add((r, c))
    
    seen_states = set() #guarda (fila, columna, dr, dc)
    
    while True:
        state = (r, c, dr, dc)
        if state in seen_states:
            #Si ya hemos visto este estado, terminamos el bucle
            break
        seen_states.add(state)
        
        nr = r + dr #new row = actual row + direction row
        nc = c + dc #new col = actual col + direction col
        #Si la nueva posición está fuera del mapa --> avanza y sales --> el bucle termina
        if not (0 <= nr < rows and 0 <= nc < cols):
            #el guardia sale fuera del mapa
            break
        
        #Si la casilla de delante es un obstaculo --> giramos a la derecha, no nos movemos
        if grid[nr][nc] == '#':
            #giro a la derecha (dr, dc) -> (dc, -dr)
            dr, dc = dc, -dr #esto quiere decir que dr = dc y dc = -dr
            continue
        
        #Si la casilla de delante es libre --> avanzamos
        r, c = nr, nc
        visited.add((r, c)) #Continuamos con la misma dirección
        
    #Construcción del mapa con X en las posiciones visitadas
    output_map = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i,j) in visited:
                row.append('X')
            else:
                row.append(grid[i][j])
        output_map.append(''.join(row))
        
    return len(visited), output_map

with open(mapa, 'r') as file:
    map_lines = [line.rstrip('\n') for line in file]
    
n_visitadas, mapa_x = simular_patrulla(map_lines)
print("Número de casillas visitadas:", n_visitadas)
print("\n".join(mapa_x))
#print(mapa_x)