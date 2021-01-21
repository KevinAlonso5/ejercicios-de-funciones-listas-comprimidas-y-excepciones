#1.Función que recibe dos enteros, a y b, y divide el mayor por el menor mostrando un mensaje de error si es una división entre cero (ZeroDivisionError).

def divisiones(num1, num2):
  try:
    if num1 > num2:
        return num1/num2
    else:
        return num2/num1
  except:
    return "ZeroDivisionError"


#2.Función que recibe una lista y el elemento a buscar, devolviendo su posición si existe, y -1 en caso de que no (ValueError) [Pista: podemos usar la función list.index(value)]

def buscar(lisValores, buscar):
    try:
        return lisValores.index(buscar)
    except:
        return -1


#3.Función que recibe una lista y calcula la suma de todos los elementos, devolviendo None en caso de que alguno de los elementos no pueda sumarse (TypeError) [Pista: ¡la función sum() está a nuestra disposición!]

def sumas(lisSum):
    try:
        return sum(lisSum)
    except:
        return "None"


#4.Función que recibe una lista y un índice, y devuelve el elemento que ocupa dicha posición o None si el índice esta fuera de los límites de la lista (¿Excepción?)

def indice (lisEntrada,i):
    try:
        return lisEntrada[i]
    except:
        return "None"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

lisPruebas= ["pepe", "juan", 55, 33.2]

print("elige el ejercicio ")

print(divisiones(10,6))

print(buscar(lisPruebas, "nom"))

print(sumas(lisPruebas))

print(indice(lisPruebas, 80))