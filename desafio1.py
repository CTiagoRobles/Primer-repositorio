#Alumno: Tiago Robles

#----------------------------------------DESAFIO 1----------------------------------------
# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura en cm: "))

if altura < 160:
    print("Su posicion es Base.")
elif altura >= 160 and altura <= 179:
    print("Su posición es Escolta.")
elif altura >= 180 and altura <= 199:
     print("Su posicion es Alero.")
else:
    print("Usted puede ser Ala-Pívot o Pívot")

# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

import random

nota = random.randint(1, 10)   #Nota para el profesor: Pude hacer esto con guias de Youtube, e IA's.


if nota >= 6:
    print(f"Promoción directa, la nota es: {nota}")
elif nota == 4 or nota == 5:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")