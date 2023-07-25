#Creamos una lista con numeros
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

#Creamos una función común que diga si es par o no
def es_par(numero):
    if (numero%2==0):
        return True
#Usando filter con la función común
numeros_pares = filter(es_par,num)
print(list(numeros_pares))

#Ahora hacemos lo mismo pero con la función lambda
numeros_pares2 = filter(lambda numero:numero%2==0,num)
print(list(numeros_pares2))