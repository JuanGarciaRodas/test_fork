# 1. Sumar todos los elementos de una lista:

# Crea una función llamada suma_elementos que reciba una lista de números como parámetro y devuelva la suma de todos sus elementos.

# Pista: Puedes utilizar una variable para acumular la suma dentro del bucle "for".
numbers=[56,89,456,98,123,987,345]
def sumaElementos(numbers):
    result =0
    for number in numbers:
        result += number
    return result    
print(numbers)

print('Esta es la suma de todos los numeros: ',sumaElementos(numbers))


# 2. Contar la cantidad de elementos pares en una lista:

# Crea una función llamada contar_pares que reciba una lista de números como parámetro y devuelva la cantidad de elementos pares que contiene.

# Pista: Dentro del bucle "for", puedes verificar si cada elemento es divisible por 2.

numeros =[2,3,7,10,35,38,12,13,15]
print(numeros)
def contar_pares(numeros):
   contador=0
   for numero in numeros:
      if numero % 2 ==0:
        contador+=1 
   return contador
print('Esta es la cantidad de pares que se encuentra en la lista: ',contar_pares(numeros))


# 3. Encontrar el elemento más grande de una lista:

# Crea una función llamada elemento_mas_grande que reciba una lista de números como parámetro y devuelva el elemento más grande de la lista.

# Pista: Puedes utilizar una variable para almacenar el elemento más grande encontrado hasta el momento.
n_Numbers=0
def elemento_mas_grande():
   pass











