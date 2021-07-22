# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Solicitar Temperaturas
print('Ingrese tres Temperaturas')
num_1 = int(input('Temperatura 1:\n')) 
num_2 = int(input('Temperatura 2:\n')) 
num_3 = int(input('Temperatura 3:\n')) 

# Promedio Temperaturas
temp_avg = (num_1 + num_2 + num_3) / 3

# Ordenar Temperaturas

if num_1 == num_2 and num_1 == num_3:
    print('Todas las Temperatutas son iguales')

elif (num_1 == num_2 or num_1 == num_3):
    if num_2 >  num_3:
        temp_1 = num_2
        temp_2 = num_3
    else:
        temp_1 = num_3
        temp_2 = num_2

elif num_2 == num_3:
    if num_1 >  num_3:
        temp_1 = num_1
        temp_2 = num_3
    else:
        temp_1 = num_3
        temp_2 = num_1

else:
    if num_1 > num_2:
        if num_1 < num_3:
            temp_1 = num_3
            temp_2 = num_2
        elif num_2 > num_3:
            temp_1 = num_1
            temp_2 = num_3
    elif num_2 > num_3:
        if num_3 > num_1:
            temp_1 = num_2
            temp_2 = num_1
        else:
            temp_1 = num_2
            temp_2 = num_3
    else:
        if num_1 > num_3:
            temp_1 = num_2
            temp_2 = num_3
        else:
            temp_1 = num_2
            temp_2 = num_1

print('La Temperatura máxima es {}°C y la mínima es {}°C'.format(temp_1, temp_2))
print('La Temperatura Promedio es {}°C'.format(temp_avg))