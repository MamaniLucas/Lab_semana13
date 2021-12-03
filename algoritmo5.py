def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total
def producto(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total
print(suma([1, 2, 3, 4]))
print(producto([1, 2, 3, 4]))

#OTRA FORMA
def suma (numeros):
    return suma(numeros)
    
def multiplicacion(numeros):
    a=1
    for i in numeros:
        a*=i
    return a
lista = [1, 2, 3, 4]
print(suma(lista))
print(multiplicacion(lista))