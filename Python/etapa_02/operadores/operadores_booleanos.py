#Definimos 2 varialbes de tipo booleanas
a=True
b=False

#OPERADORES:
#AND: nos devuelve True siempre que todas las condiciones sean verdaderas.
print(f'El operador (a and a) nos da como resultado: {a and a}') #Devuelve True
print('---------------------------------------------------------')

print(f'El operador (a and b) nos da como resultado: {a and b}') #Devuelve False
print('---------------------------------------------------------')

#OR: nos devuelve True si alguna de las condiciones es verdadera.
print(f'El operador (a or b) nos da como resultado: {a or b}') #Devuelve True
print('---------------------------------------------------------')

#NOT: niega el valor que nos esté devolviendo una evaluación booleana
resultado = a and a #Esta variable resultado contiene el valor True
print(f'La variable resultado es igual a: {resultado}') #Devuelve True
print('-------------------------------------------------------------')

print(f'La variable resultado (con el operador NOT) es igual a: {not resultado}') #Devuelve Devuelve Falso
print('-------------------------------------------------------------')

resultado = a and b #Esta variable resultado contiene el valor False
print(f'La variable resultado es igual a: {resultado}') #Devuelve False
print('-------------------------------------------------------------')

print(f'La variable resultado (con el operador NOT) es igual a: {not resultado}') #Devuelve Devuelve True
print('-------------------------------------------------------------')
