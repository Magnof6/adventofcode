

def encontrar_pos_inicial(map_lines):
    for r, row in enumerate(map_lines): #Enumerate para obtener el índice y el valor
        for c, ch in enumerate(row): #nos devuelve el indice y el caracter en esa posición
            if ch in '^>v<':
                return (r, c), ch
    return None, None

def simular_patrulla(map_lines):
    dirs = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    grid = [list(row) for row in map_lines]
    start, symbol = encontrar_pos_inicial(map_lines)
    dr, dc = dirs[symbol]
    r, c = start
    visited = set([(r,c)])
    seen_states = set()

    while True:
        state = (r, c, dr, dc)
        if state in seen_states:
            return True  # bucle detectado
        seen_states.add(state)

        nr, nc = r + dr, c + dc
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            return False  # salió del mapa

        if grid[nr][nc] == '#':
            dr, dc = dc, -dr  # girar a la derecha
            continue

        r, c = nr, nc
        visited.add((r,c))

def posiciones_candidatas(map_lines):
    start, _ = encontrar_pos_inicial(map_lines)
    candidatos = []
    for r, row in enumerate(map_lines):
        for c, ch in enumerate(row):
            if ch == '.' and (r,c) != start:
                # prueba con obstáculo temporal
                test_map = [list(line) for line in map_lines]
                test_map[r][c] = '#'
                test_map = [''.join(line) for line in test_map]
                if simular_patrulla(test_map):
                    candidatos.append((r,c))
    return candidatos

# ---- Uso ----
with open("map.txt") as f:
    map_lines = f.read().splitlines()

candidatos = posiciones_candidatas(map_lines)
print("Número de posiciones que causan bucle:", len(candidatos))
print("Posiciones candidatas:", candidatos)
