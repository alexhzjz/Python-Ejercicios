'1. Ejercicios de Listas con For en Python'

def suma_elementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo
numeros = [100, 200, 300, 400, 500]
resultado = suma_elementos(numeros)
print("La suma de los elementos es:", resultado)

'2. Contar la cantidad de elementos pares en una lista:'
def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

# Ejemplo
numeros = [16, 20, 38, 40, 50, 60]
resultado = contar_pares(numeros)
print("La cantidad de elementos pares es:", resultado)

'3. Encontrar el elemento más grande de una lista:'
def elemento_mas_grande(lista):
    if not lista:  # Verifica si la lista está vacía
        return None
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Ejemplo
numeros = [1, 2, 3, 4, 5, 6]
resultado = elemento_mas_grande(numeros)
print("El elemento más grande de la lista es:", resultado)

'4. Crear una nueva lista con los elementos de otra lista multiplicados por 2:'
def multiplicar_elementos(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero * 2)
    return nueva_lista

# Ejemplo
numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_elementos(numeros)
print("La nueva lista con los elementos multiplicados por 2 es:", resultado)

'5. Invertir una lista:'
def invertir_lista(lista):
    nueva_lista = []
    for elemento in reversed(lista):
        nueva_lista.append(elemento)
    return nueva_lista

# Ejemplo
numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print("La lista invertida es:", resultado)