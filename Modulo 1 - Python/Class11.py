#Ejercicio 1. Genere un programa que reciba un entero n, entre 1 y 20, y que imprima el cubo de los numeros desde 1 hasta n, espaciados por un final de linea, avanzando de 1 en 1.
"""
number=int(input("Numero: "))

#Metodo 1
number2=1
while number >= 1:
    print(number2**3)
    number-=1
    number2+=1

#Metodo 2
for i in range(1,number+1):
    print(i**3)


#Ejemplo While con Listas

mylist=[]

while number>=1:
    mylist.append(number**3)
    number-=1
mylist.reverse()
print(mylist)
"""
#Ejercicio 2. Los palindromo son frases que se leenigual de derecha a izquierda y vicerversa. Por ejemplo "anita lava la tina" es un palindromo, ya que
#obviando los espacios en blanco, la frase se lee igual. Elabora un programaque diga si es una frase en palindromo o no.

frase=input("Escriba la frase a evaluar: ").replace(" ", "")

mylist=[]
mylist2=[]

for i in frase:
    mylist.append(i)
    mylist2.append(i)

mylist2.reverse()

print("Lista 1")
print(mylist)
print("Lista 2")
print(mylist2)

if mylist==mylist2:
    print("Es Palindrono")
else:
    print("No es palindromo")



#Ejercicio 3. Calcula el impuesto de una propiedad mediante la formula impuesto=valorpropiedad*0.0065
#Para esto el usuario debe digitar el numero del lote de la propiedad y luego el valor, si el usuario escribe 0, salir.

lote=(int(input("Numero del lote: ")))
valor=(int(input("Valor del inmueble: $")))
is_valid=True

while is_valid:
    if lote>0:
        impuesto=valor*0.0065    
        print(f"Impuestos: ${impuesto}")
        lote=(int(input("Numero del lote: ")))
        valor=(int(input("Valor del inmueble: $")))
        is_valid=True
    else:
        is_valid=False






"""
Metodos

.reverse(): Revierte el orden de una lista
.append(x): Agrega el valor x al final de una lista
.len(String o List): Metodo que me dice la cantidad de caracteres o elementos que tiene un String o Lista
.type(x): Evalua el tipo de variable que esta contenido en la variable x.
"""