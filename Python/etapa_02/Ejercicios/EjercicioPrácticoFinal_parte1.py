# Defino una variable que contenga una lista con los salarios de Juan
salarios_juan = [300] * 6 + [500] * 4 + [700] * 2

#Creo 2 funciones para calcular el sueldo promedio y clasificar el mismo según los parámetros solicitados
def calcular_sueldo_promedio(salarios):
    total_salarios = sum(salarios)
    sueldo_promedio = total_salarios / len(salarios)
    return sueldo_promedio

def clasificar_sueldo(sueldo_promedio):
    if sueldo_promedio < 300:
        return "Sueldo bajo"
    elif sueldo_promedio <= 900:
        return "Sueldo normal"
    else:
        return "Sueldo mejor de lo normal"

# Calculo el sueldo promedio
sueldo_promedio_juan = calcular_sueldo_promedio(salarios_juan)

# Clasifico el sueldo
categoria_sueldo_juan = clasificar_sueldo(sueldo_promedio_juan)

# Finalmente, muestro los resultados
print(f"El sueldo promedio de Juan es: {sueldo_promedio_juan:.2f} dólares")
print(f"Categoría de sueldo de Juan: {categoria_sueldo_juan}")
