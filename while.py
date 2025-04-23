#explicacion y uso de while


# clave=3344
# password=int (input("ingrese su pass:"))
# while clave!=password:
#     print ("error, clave invalida")
#     password=int(input("ingrese su pass:"))


# print("bienvenido al sistema")

#clave con 3 intentos

clave=3344
intentos=0
password=int (input("ingrese su pass:"))
while clave!=password and intentos<=3:
    print ("error, clave invalida")
    intentos=intentos+1
    password=int(input("ingrese su pass:"))
if intentos>=3:
    print ("ha alcanzado la cantidad maxima de intentos")
else:
    print("bienvenido al sistema")