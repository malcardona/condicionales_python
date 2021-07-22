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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

# Solicitar Palabras
print('Ingrese tres Palabras')
texto_1 = str(input('Palabra 1:\n')) 
texto_2 = str(input('Palabra 2:\n')) 
texto_3 = str(input('Palabra 3:\n')) 

# Consultar como ordenar palabras
print('Como desea ordernar las palabras?')
print('1- Orden Alfabético')
print('2- Cantidad de Palabras')

ord = str(input())

# Comprobar que la opcion ingresada sea correcta
if (ord != '1' ) and (ord != '2'):
    print('Debe ingresar una opción válida')
    ord = str(input())

# Orden Alfabético
if ord == '1':
    print('Se ordenaran las palabras en Orden Alfabético')

    # Si todas las Palabras son iguales
    if texto_1 == texto_2 and texto_2 == texto_3:
       print('Todas las palabras son iguales')
    
    # Si dos palabras son Iguales
    elif (texto_1 == texto_2 or texto_1 == texto_3):
        if texto_2 > texto_3:
            p_1 = texto_2
            p_2 = texto_1
            p_3 = texto_3
        else:
            p_1 = texto_3
            p_2 = texto_1
            p_3 = texto_2
        print('{} > {} > {}'.format(p_1, p_2, p_3))

    elif texto_2 == texto_3:
        if texto_1 > texto_3:
            p_1 = texto_1
            p_2 = texto_2
            p_3 = texto_3
        else:
            p_1 = texto_3
            p_2 = texto_2
            p_2 = texto_1
        print('{} > {} > {}'.format(p_1, p_2, p_3))

    # Todas las palabras diferentes
    else:
        if texto_1 > texto_2:
            if texto_1 < texto_3:
                p_1 = texto_3
                p_2 = texto_1
                p_3 = texto_2
            elif texto_2 > texto_3:
                p_1 = texto_1
                p_2 = texto_2
                p_3 = texto_3
        elif texto_2 > texto_3:
            if texto_3 > texto_1:
                p_1 = texto_2
                p_2 = texto_3
                p_3 = texto_1
            else:
                p_1 = texto_2
                p_2 = texto_1
                p_3 = texto_3
        else:
            if texto_1 > texto_3:
                p_1 = texto_2
                p_2 = texto_1
                p_2 = texto_3
            else:
                p_1 = texto_2
                p_2 = texto_3
                p_2 = texto_1
        print('{} > {} > {}'.format(p_1, p_2, p_3))
