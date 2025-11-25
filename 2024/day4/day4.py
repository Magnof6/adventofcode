
df = "memory.txt"
def contar_XMAS(memoria):
    with open(memoria, 'r') as file:
        data = file.read().splitlines() #lista de strings una por fila
        word = "XMAS"
        rows = len(data)
        cols = len(data[0])
        count = 0
        
        directions = [
            (0, 1),   # → derecha
            (0, -1),  # ← izquierda
            (1, 0),   # ↓ abajo
            (-1, 0),  # ↑ arriba
            (1, 1),   # diagonal ↓→
            (1, -1),  # diagonal ↓←
            (-1, 1),  # diagonal ↑→
            (-1, -1)  # diagonal ↑←
        ]
        
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    found =  True
                    for k in range(len(word)):
                        nr = r + dr * k
                        nc = c + dc * k
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or data[nr][nc] != word[k]:
                            found = False
                            break
                    if found:
                        count += 1
        return count

print("Total de XMAS encontrados es:", contar_XMAS(df))