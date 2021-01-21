personas = ["Sara", "Pedro", "Miguel"]
x = [8, 2, 3, -1, 2, -5, 7]

#1.El cubo de cada elemento de la lista x.
salida= [i**3 for i in x]
print(salida)

#2.El cuadrado de los elementos impares de x.
salida= [i ** 2 for i in x if i % 2 != 0]
print(salida)

#3.El cuadrado de los elementos pares y positivos de x.
salida= [i**2 for i in x if i%2 == 0 and i > 0]
print(salida)

#4.Los elementos de personas con más de 5 caracteres.
salida = [i for i in personas if len(i)>5] 
print(salida)

#5.Los elementos de personas que contienen la vocal “o”.
salida = [i for i in personas if "o" in i] 
print(salida)

#6.Los elementos de personas que contienen la vocal “e” y además tienen una longitud de al menos 6 caracteres.
salida = [i for i in personas if "a" in i and len(i)>5]
print(salida)