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
        
def calcular_mull_condicional(memoria):
    with open(memoria, 'r') as file:
        data= file.read()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
        matches = re.finditer(pattern, data)
        total = 0
        enabled = True
        for m in matches:
            if m.group(0) == "do()":
                enabled = True
            elif m.group(0) == "don't()":
                enabled = False
            else:
                x,y = m.groups()
                total += int(x) * int(y) if enabled else 0
        return total

print("Total de la suma es:", calcular_mull(df))
print("Total condicional de la suma es:", calcular_mull_condicional(df))