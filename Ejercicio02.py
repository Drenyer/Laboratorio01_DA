print("Ingrese un numero entero \n ")
numero=int(input("-->"))
suma=0
a=1
while a <= numero:
    suma+=a
    a+=1

print("La suma de numeros antecedentes al ingresado es: "+str(suma))