#1.Función que recibe una lista de enteros y devuelve la suma de todos sus elementos. Sin utilizar sum().
def sumaEnteros(listaNum):
    i = 0
    suma = 0
    while i < len(listaNum):
        suma = suma + listaNum[i]
        i = i + 1
    return suma


#2.Función que recibe una lista de enteros y devuelve otra lista con aquellos que son pares y ≥ 113.
def numPares(listaNum):
    i = 0
    salida = []
    while i < len(listaNum):
        if listaNum[i] % 2 == 0 and listaNum[i] >= 113:
            salida.append(listaNum[i])
        i = i + 1
    return salida


#3.Función que recibe una lista de enteros y calcula su media aritmética sin utilizar el módulo maths
def mediaArig(listaNum):
    i = 0
    suma = 0
    while i < len(listaNum):
        suma = suma + listaNum[i]
        i = i + 1
    return suma / len(listaNum)


#4.Función que calcula el factorial de un número. Versión recursiva.
def factorial(num1):
    salida = 1
    i = 1
    while i <= num1:
        salida = salida * i
        i = i + 1
    return salida


#5.Función que recibe un número y devuelve una lista con todos sus divisores.
def divisores(num1):
    salida = []
    i = 1
    while i <= num1:
        if num1 % i == 0:
            salida.append(i)
        i = i + 1
    return salida


#6.Función que determina si un número es primo o no (devuelve True o False).
def primo(num1):
    salida = []
    i = 1
    while i <= num1:
        if num1 % i == 0 and i != num1 and i != 1:
            return False
        i = i + 1
    return True



#7. Crear una función que calcule el MCD de dos números por el método de Euclides.
def calcularMCD(num1, num2):
    mallor, menor = intercambiar(num1, num2)
    resto = int(mallor) % int(menor)
    if resto == 0:
        return menor
    else:
        return calcularMCD(menor, resto)


#
def intercambiar(mallor, menor):
    if mallor < menor:
        return menor, mallor
    else:
        return mallor, menor


#-------------------------------------------------------------------------------

valPrueba = [50, 25, 13, 20,150]


print(sumaEnteros(valPrueba))

print(numPares(valPrueba))

print(mediaArig(valPrueba))

print(factorial(5))

print(divisores(25))

print(primo(21))

print(calcularMCD(125, 25))
