'Ejercicios con While y Colecciones en Python'
'1. Eliminar duplicados de una lista:'
def eliminar_duplicados(lista):
    conjunto_unico = set()
    nueva_lista = []
    indice = 0
    
    while indice < len(lista):
        elemento = lista[indice]
        if elemento not in conjunto_unico:
            conjunto_unico.add(elemento)
            nueva_lista.append(elemento)
        indice += 1
    
    return nueva_lista

# Ejemplo
numerosrepetidos = [10, 2, 2, 2, 4, 4, 89]
resultado = eliminar_duplicados(numerosrepetidos)
print("La lista sin duplicados es:", resultado)

'2. Adivinar un número con intentos limitados:'
import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 7
    adivinado = False

    print("Bienvenido al juego de adivinanza!!!")
    print("He generado un número entre 1 y 100. Tienes 7 intentos para adivinarlo - Animo!!!.")

    while intentos_restantes > 0 and not adivinado:
        intento = int(input("Introduce tu intento: "))
        intentos_restantes -= 1

        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            adivinado = True
            print("¡Felicidades! Has adivinado el número.")

        if not adivinado:
            print(f"Te quedan {intentos_restantes} intentos.")

    if not adivinado:
        print(f"Lo siento, te has quedado sin intentos. El número secreto era {numero_secreto}.")

# Ejecutar el juego
adivina_el_numero()
'3. Contar vocales en una frase:'
def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    indice = 0

    while indice < len(frase):
        if frase[indice] in vocales:
            contador += 1
        indice += 1

    return contador

# Ejemplo
frase = input("Ingresa una frase: ")
cantidad_vocales = contar_vocales(frase)
print("La cantidad de vocales en la frase es:", cantidad_vocales)

'4. Calculadora básica:'
def calculadora():
    while True:
        print("\nCalculadora Básica")
        print("Selecciona una operación:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")

        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Byeeee!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                resultado = num1 + num2
                print(f"El resultado de {num1} + {num2} es {resultado}")
            elif opcion == '2':
                resultado = num1 - num2
                print(f"El resultado de {num1} - {num2} es {resultado}")
            elif opcion == '3':
                resultado = num1 * num2
                print(f"El resultado de {num1} * {num2} es {resultado}")
            elif opcion == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"El resultado de {num1} / {num2} es {resultado}")
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar la calculadora
calculadora()

'5. Crear una lista de números pares:'
# Inicializo la lista vacía
numeros_pares = []

# Inicializo el contador
contador = 1

# Bucle while para recorrer los números del 1 al 100
while contador <= 100:
    # Verifico si el número es par
    if contador % 2 == 0:
        # Agrego el número par a la lista
        numeros_pares.append(contador)
    # Incremento el contador
    contador += 1

# Imprimo la lista de números pares
print(numeros_pares)