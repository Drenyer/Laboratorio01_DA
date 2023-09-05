print("Ingrese una lista de numero enteros")
lista=[]
a=1
while a<5:
    a+=1
    numeros=int(input("-->"))
    lista.append(numeros)
    print("Sucessfull")
print(lista)
maximo=max(lista)
print("El numero mayor es:"+str(maximo))