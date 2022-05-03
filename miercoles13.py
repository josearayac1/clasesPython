#Ejercicio 01
""" mensaje = "Bienvenido al mundo de la programacion"
print(f"{mensaje}") """

""" print("Bienvenid@ al mund@ de la programacion") """

#Ejercicio 01 B y 02A
""" nom=input("ingresa tu nombre: ")
print(f"Bienvenido {nom}") """

#Ejercicio 03
""" x = int(input("ingrese valor para resolver la ecuacion (x^2 + 3x + 1)/4: " ))
resultado = (x**2 + 3*x + 1)/4
print(f"el resultado \nde la ecuacion con el numero \n{x} es igual a \n{resultado}")
 """
#Ejercicio 04
""" nombre = input("ingrese su nombre: ")
rut = input("ingrese su rut: ")
correo = input("ingrese su correo: ")
celular = int(input("ingrese numero telefonico: "))
print("--------RESUMEN-------")
print(f"NOMBRE: {nombre} \nRUT: {rut} \nCORREO: {correo} \nCELULAR: {celular}")
print("----------------------") """

#COMO MANEJAR OTRO TIPO DE DATO
""" decimal = (input("ingrese numero decimal"))
print(f"{decimal}")
print(type(decimal)) """

#sintaxis if, elif y else
#Actividad 2 ejercicio 01
"""edad = int(input("ingrese su edad"))
 if edad >= 18 and edad < 110:
    print("usted es mayor de edad")
elif edad <18 and edad >0 :
    print("usted es menor de edad ")
else:
    print("no existe edad, ingrese nuevamente") """
    
#Actividad 2 ejercicio 02
""" user01 = "pedro"
pass01 = 4
user02 = "angel"
pass02 = 32

user0 = input("ingrese nombre de usuario: ")
pass0 = int(input("ingrese clave de usuario: "))

if user0 == user01 and pass0 == pass01 :
    print("Bienvenido Pedro")
elif user0 == user02 and pass0 == pass02 :
    print("Bienvenido Angel")
else:
    print("credenciales incorrectas") """


#Actividad 2 ejercicio 03
""" from decimal import Rounded
from os import truncate


nota1 = float(input("ingrese su primera nota: "))
nota2 = float(input("ingrese su segunda nota: "))
nota3 = float(input("ingrese su tercera nota: "))

promedio = round((nota1 + nota2 + nota3)/3,1)

if promedio >= 4.0:
    print(f"felicitaciones, esta aprobado con una nota de {promedio}")
else:
    print(f"lo siento, esta reprobado con una nota de {promedio}") """