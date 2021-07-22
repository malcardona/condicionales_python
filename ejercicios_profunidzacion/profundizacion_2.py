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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Ingresar Números
print('Ingrese tres números entreros')
num_1 = int(input(' número 1:\n')) 
num_2 = int(input(' número 2:\n')) 
num_3 = int(input(' número 3:\n')) 

# Prueba par-impar

if (num_1 % 2) == 0:
    print('El primer numero es par')
else:
    print('El primer numero es impar')
    
if (num_2 % 2) == 0:
    print('El segundo numero es par')
else:
    print('El segundo numero es impar')
    
if (num_3 % 2) == 0:
    print('El tercer numero es par')
else:
    print('El tercer numero es impar')

    