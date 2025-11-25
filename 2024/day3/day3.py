import re
df = "memory.txt"

def calcular_mull(memoria):
    with open(memoria, 'r') as file:
        data = file.read()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, data)
        total = 0
        for x, y in matches:
            total += int(x) * int(y)
        return total
        

print("Total de la suma es:", calcular_mull(df))