
#Leccion 1

                                #Variables

char='a' #Esto es un caracter
print(char)
string="Hola Mundo" #Esto es una cadena de caracteres
print(string)
int=5 #Esto es un entero
print(int)
float=2.8 #Esto es un número flotante
print(float)
boolean=True #Esto es un boleano
print(boolean)

                                #Math

#Variables para utilizar
my_int=5 
my_float=2.0
my_char="*" 

#Esto es una suma
var=my_int+my_float
print(var)

#Esto es una resta
var=my_int-my_float
print(var)

#Esto es una multiplicacion
var=my_int*my_float
print(var)

#Esto es una division
var=my_int/my_float
print(var)

#Otros
var=my_char*my_int
print(var)

                                #Logic Ops
#Menor que
var=my_int<my_float
print(var)
#Mayor que
var=my_int>my_float
print(var)
#Menor o igual que
var=my_int<=my_float
print(var)
#Mayor o igual que
var=my_int>=my_float
print(var)
#Igual que
var=my_int==my_float
print(var)
#Diferente que
var=my_int!=my_float
print(var)

                                #Prints

name="Max"
surname="Jimenez"

print(name+" "+surname)

print(name, surname)

print(name, surname, end="! ")

print(f"{name} {surname}")

print("{} {}".format(name, surname))

#Ejercicio 1. Imprimir Meses del año de manera indirecta
var1="Enero"
var2="Febrero"
var3="Marzo"
var4="Abril"
var5="Mayo"

print("{} {} {} {} {}".format(var1,var2,var3,var4,var5))

#Ejercicio 2. Formatea el texto usando las siguientes variables
name1="Max Jimenez"
email1="mjp@gmail.com"
address1="Carrera 8#35B-67"

print(f"Name:{name1}\nEmail:{email1}\nAdrress:{address1}")

#Ejercicio 3. Formatea el texto solicitando las siguientes variables
name2=input("Escribe tu nombre ")
email2=input("Escribe tu email ")
address2=input("Escribe tu dirección de domicilio ")

print(f"Name:{name2}\nEmail:{email2}\nAdrress:{address2}")