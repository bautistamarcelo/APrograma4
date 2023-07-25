#creando una función simple 
def saludo():
    print('Hola Mundo')
    
#Llamando a la función simple creada
saludo()

#Creando la función pero con parámetros
def saludo_segun(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo="mi Reina"
    elif sexo == "hombre":
        adjetivo = "Kapo"
    else:
        adjetivo = "mi amor"
    
    print(f'Hola {nombre} {adjetivo},¿como estás?')

#Llamando a la función con parámetros
saludo_segun("MARCELO","MASCULINO")

#Creando una función que nos retorne valores
def crear_contraseña_random(numero):
    crt = 'abcdefghij'
    n_ent = str(numero)
    numero = int(n_ent[0]) #Esto es para obtener sólo el primer dígito del numero pasado por parametro
    if numero <=0:
        c1 = 0
        c2 = numero
        c3 = numero + 3
    elif numero>=2:
        c1 = numero-2
        c2 = numero
        if numero <=5:
            c3 = numero + 3
        else:
            c3 = numero
    else:
        c1 = 1
        c2 = numero
        c3=2
        
    contraseña = f'{crt[c1]}{c1}{crt[c2]}{c2}{crt[c3]}{c3}{c1}'
    return contraseña, numero

#Desempaquetando la función

password, primer_num = crear_contraseña_random(521)

#Mostrando los resultados de la función
print(f'tu nueva contraseña es: {password}')
print(f'El número utilizado para obtenerla fue: {primer_num}')