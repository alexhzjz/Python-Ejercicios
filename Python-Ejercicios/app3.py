'Ejercicios con Diccionarios'
'1. Crear un diccionario de alumnos y sus notas:'
# Inicializo el diccionario vacío
estudiante = {}

# Bucle while para ingresar datos del estudiante
while True:
    # Pido al usuario el nombre del alumno
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
    
    # Verificar si el usuario quiere salir
    if nombre.lower() == 'salir':
        break
    
    # Pedir al usuario la nota del alumno
    nota = input(f"Ingrese la nota de {nombre}: ")
    
    # Almacena la información en el diccionario
    estudiante[nombre] = nota

# Mostrar el diccionario con todos los alumnos y sus notas
print("\nDiccionario de alumnos y sus notas:")
print(estudiante)

'2. Calcular el promedio de las notas de un diccionario:'
def promedio_notas(alumnos):
    # Inicializo la suma de las notas
    suma_notas = 0
    
    # Se recorre las notas del diccionario
    for nota in alumnos.values():
        suma_notas += float(nota)
    
    # Calcula el promedio
    promedio = suma_notas / len(alumnos)
    
    return promedio

# Ejemplo
alumnos = {
    "Juan": 4.5,
    "María": 3.8,
    "Pedro": 4.2,
    "Ana": 3.9
}

promedio = promedio_notas(alumnos)
print(f"El promedio de las notas es: {promedio:.2f}")

'3. Encontrar al alumno con la nota más alta:'
def alumno_con_mejor_nota(alumnos):
    # Inicializo las variables para el nombre y la nota más alta
    mejor_alumno = None
    mejor_nota = -1
    
    # Se recorre el diccionario de alumnos y notas
    for nombre, nota in alumnos.items():
        # Convertir la nota a float y comparar con la mejor nota actual
        if float(nota) > mejor_nota:
            mejor_nota = float(nota)
            mejor_alumno = nombre
    
    return mejor_alumno

# Ejemplo
alumnos = {
    "Juan": 4.5,
    "María": 3.8,
    "Pedro": 4.2,
    "Ana": 3.9
}

mejor_alumno = alumno_con_mejor_nota(alumnos)
print(f"El alumno con la mejor nota es: {mejor_alumno}")

'4. Crear un diccionario de palabras y sus definiciones:'
# Inicializo el diccionario vacío
diccionario = {}

# Bucle while para ingresar palabras y definiciones
while True:
    # Pedir al usuario la palabra
    palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
    
    # Verifico si el usuario quiere salir
    if palabra.lower() == 'salir':
        break
    
    # Pido al usuario la definición de la palabra
    definicion = input(f"Ingrese la definición de '{palabra}': ")
    
    # Almaceno la información en el diccionario
    diccionario[palabra] = definicion

# Muestro el diccionario con todas las palabras y sus definiciones
print("\nDiccionario de palabras y sus definiciones:")
for palabra, definicion in diccionario.items():
    print(f"{palabra}: {definicion}")

'5. Buscar una palabra en un diccionario:'
def buscar_palabra(diccionario, palabra):

    # Busco la palabra en el diccionario
    definicion = diccionario.get(palabra)
    
    # Verifico si la palabra se encontró
    if definicion:
        return definicion
    else:
        return "La palabra no se encontró en el diccionario."

# Ejemplo
diccionario = {
    "Python": "Un lenguaje de programación de alto nivel.",
    "Computador": "Aparato electronico.",
    "Televisor": "Aparato para ver programas."
}

palabra_a_buscar = "Python"
resultado = buscar_palabra(diccionario, palabra_a_buscar)
print(f"Definición de '{palabra_a_buscar}': {resultado}")

palabra_a_buscar = "Amor"
resultado = buscar_palabra(diccionario, palabra_a_buscar)
print(f"Definición de '{palabra_a_buscar}': {resultado}")