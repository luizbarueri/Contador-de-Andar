#calculadora simples
def calculadora(a,b, operador):
    total = 0
    if operador == "+": total = a + b
    if operador == "-": total = a - b
    if operador == "*": total = a * b
    if operador == "/" and b > 0: total = a / b
    return total

print("Somar:" ,calculadora(5,7, "+"))
print("Subtrair:", calculadora(5,7, "-"))
print("Multiplicar:", calculadora(5,7, "*"))
print("Dividir", calculadora(5,7, "/"))