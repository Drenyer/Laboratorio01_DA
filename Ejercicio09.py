print("Conteo de vocales \n")
cadena = input("Ingrese una frase: ").lower() 
vocales = 0
if "a" in cadena:
    vocales +=cadena.count("a")
if "e" in cadena:
    vocales +=cadena.count("e")
if "i" in cadena:
    vocales +=cadena.count("i")
if "o" in cadena:
    vocales +=cadena.count("i")
if "u" in cadena:
    vocales +=cadena.count("u")
print("La cantidad de vocales que hay es: " + str(vocales))