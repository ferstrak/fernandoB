
# nombre="diego"
# edad=25
# print ("hola",nombre, "su edad es",edad)

# function (argumento de la funccion)



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# solicitud de datos
# print ("ingrese su nombre")
# nombre=input()
# print ("ingrese su edad")
# edad=input()
# # ejemplo de concatenación
# print ("hola",nombre, "su edad es",edad)
# print ("ingrese 2 numeros ")
# 7
# n1=int(input())
# n2=int(input())
# print ("el resultado es", n1 + n2)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# print ("ingrese 3 numeros para promedio ")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# prom=(n1+n2+n3)/3
# print ("el promedio es",prom)

# if prom>=40:
#     print("el alumno aprobo")
# else:
#     print("el alumno reprobo")    
# /////////////////////////////////////////////////////////////////////////////////////////////////
# print ("ingrese su nombre")
# nombre=input()
# edad =int(input("ingrese su edad")) 


# if edad>=18:
#    print ("mayor de edad")
# else:
#    print ("menor de edad")


# ////////////////////////////////////////////
# edad =int(input("ingrese su edad")) 
# if edad<12:
#    print ("usted es un niño")
# elif edad >=12 and edad<18:
#    print ("usted es un adolescente")
# elif edad >=18 and edad<65:
#    print ("usted es un adulto")  
# else:
#    print ("usted es un viejo")

# //////////////////////////////////////////////////////////////////////////////////

# print ("ingrese 3 numeros")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2 and n1>n3:
#  print (n1,"es mayor")
# elif n2>n1 and n2>n3:
#  print (n2,"es mayor") 
# else:
#  print (n3,"es mayor") 
# //////////////////////////////////////////////////////////////////////////////////

# miversion

# clave= int(11223)
# print ("ingrese su contraseña")
# contra=int(input())
# if contra==clave:
#   print ("contraseña correcta")
# else:
#   print ("contraseña incorrecta")  

# # version profe

# clave=3344
# pas=int(input("ingrese su contraseña")) 
# if pas==clave:
#   print ("contraseña correcta")
# else:
#   print ("contraseña incorrecta") 
# ////////////////////////////////////////////////////////////////////////////////////////
# inicio for 
# todoso los indices comienzan en 0 lo otro es que muestre donde tu quieres que comience pero todos los indices comienzan en 0

# pide un numero al usuario y muestra cantidad de repeticiones
# num=int(input("ingrese un numero"))
# for i in range(num):
#   print ("repeticion",i+1) #indice comienza en 0 por eso se suma 1

# pide un numero al usuario y muestra la tanla de ese numero hasta el 10
# "mi version"


# num=int(input("ingrese un numero"))
# for i in range(num):
#   print (num, "x", i+1, "=", num*(i+1))

# "profe"


# for i in range(1,11):
#    print (num, "x", i+1, "=", num*(i+1))
# ////////////////////////////////////////////////////////////////////////////////////////////////
# generacion automatica de las tablas del 10
# for i in range (10):
#   for j in range (10):
#     print (j+1,"x",i+1,"=", (i+1)*(j+1))
# ////////////////////////////////////////////////////////////////////////////////////////////

# pedir al usuario la canitdad de notas  y generar promedio
# cant=int(input("ingrese el numero de notas "))
# suma=0   # para que comience en 0
# for i in range (cant):
#     print ("ingrese nota", i+1)
#     nota=int(input())                   #float en vez de int para decimales
#     suma=suma+nota                             #suma+=nota
# prom=suma/cant
# print ("el promedio es", prom)
# //////////////////////////////////////////////////////////////////////

#pida la cantidad de alumnos y luego la cantidad de notas por alumno
# muestra el promedio de cada uno
# cantA=int(input("ingrese el numero de alumnos"))

# for j in range (cantA):
#     cantN=int(input("ingrese el numero de notas del alumno",j+1))
#     suma=0   
#     for i in range (cantN):
#         print ("ingrese nota", i+1 "del alumno",j+1,"use valores decimales")
#         nota=float(input())                   
#         suma=suma+nota                            
#     prom=suma/cantN
#     print ("el promedio es", prom)
#     if prom>=4:
#         print ("usted aprobo")
#     else:
#         print ("ustred reprobo")        
# //////////////////////////////////////////////////////////////////////////////

#pida al usuario un numero y sume todos los digitos desde el 1 hasta ese numero mostrando la suma
# num=int(input("ingrese el numero"))
# for i in range (num)
#     suma+=i+1
# print ("la suma de los numeros es",suma)  

# #pares y impares

# num=int(input("ingrese el numero"))
# if num % 2==0:
#     print ("el numero",num , "es par")
# else:
#     print ("el numero",num , "es impar") 

#pida una cantidad de numeros y vea de esos numeros cual es par y impar

#yo

# cant=int(input("ingrese la cantidad de numeros"))
# suma=0
# for i in range (cant):
#     suma+=i+1
#     if cant% 2==0:
#     print ("el numero",cant , "es par")
# else:
#     print ("el numero",cant, "es impar") 


#profe
# cant=int(input("ingrese la cantidad de numeros"))
# for i in range (cant):
#     num=int(input("ingrese un numero"))

#     if num% 2==0:
#         print ("el numero",num , "es par")
# else:
#     print ("el numero",num, "es impar") 
# /////////////////////////////////////////////////////////////////////////////////////////////

#  definir 2 candidatos. preguntar la cantidad de votantes
# preguntar a cad votante por quien votara mostrando las alternativas 
# contar votos y resultados
# definir el ganador y considerar un empate
# c1= "aqua"
# c2= "koku"
# cv1=0
# cv2=0
# cantV=int(input("cuantos votantes son? :"))

# for i in range (cantV):
#     print(f"por quien votara? 1.-{c1}, 2.- {c2}")     #f es para variables encorchetadas se pone antes de comas
#     voto=int(input())
#     if voto==1:
#         cv1=cv1+1
#         print ("ha votado por", c1)
#     else:
#         cv2=cv2+1
# print(f"la cantidad de votos de {c1} es {cv1}")
# print(f"la cantidad de votos de {c2} es {cv2}")
# if cv1>cv2:
#     print(f"gano{c1}")
# elif cv1<cv2:
#     print(f"gano{c2}")
# else:
#     print ("es un empate")
#////////////////////////////////////////////////////////////////////////////

# frase=input("ingrese una frase")
# c=0
# cons=0
# v=0
# for i in frase:
#     # #print(i)
#     if i.lower() in "aeiou":        #lower para todo minusculas upper para todo mayusculas
#         v=v+1
#     elif i.lower()=="" :  
#      cons=cons+1
        
#     c=c+1
# print ("la cantidad de caracteres es", c) 
# print ("la cantidad de vocales", v) 
# print ("la cantidad de consonantes es", cons) 
#//////////////////////////////////////////////////////////////////ver crpeta del 17

##################version alternativa#############################
# num=int(input("ingrese un numero"))
# for i in range(num):
   
#     if (i+1) %2==0:
#         print (f"el numero {i+1} es par")
       
#     else:
#         print(f"el numero {i+1} es impar")
####################version profe##################################
# for i in range(num):
   
#    if (i) %2==0:
#         print (f"el numero {i} es par")
       
#   else:
#         print(f"el numero {i} es impar")
# //////////////////////////////////////////////////////////////
# ejercicio de supermercado de pseint a python
# cant=int(input("cuanto productos llevara"))
# op=0

# for i in range(cant):
#     print("""
#         que producto llevara?
#         1.- diazepam $9000
#         2.- metametozona $18500
#         3.- oblea china $1000    
#           """)
#     op=int(input()):
#     if op==1:
#         print ("usted lleva diazepam")
#         total=total+9000
#     elif op==2:
#      print ("usted lleva metametozona")
#      total=total+18500
#      elif op==3:
#      op==3:print ("usted lleva oblea china")
#      total=total+1000
#     else:
#        print ("seleccione una opción valida") 
# print("el total neto es",total)
# print("el total neto mas iva es",total*1.19)
# ////////////////////////////////////////////////////////////////////////////////////
#explicacion y uso de while


# clave=3344
# password=int (input("ingrese su pass:"))
# while clave!=password:
#     print ("error, clave invalida")
#     password=int(input("ingrese su pass:"))


# print("bienvenido al sistema")

#clave con 3 intentos

# clave=3344
# intentos=0
# password=int (input("ingrese su pass:"))
# while clave!=password and intentos<=3:
#     print ("error, clave invalida")
#     intentos=intentos+1
#     password=int(input("ingrese su pass:"))
# if intentos>=3:
#     print ("ha alcanzado la cantidad maxima de intentos")
# else:
#     print("bienvenido al sistema")             
# /////////////////////////////////////////////////////////////////////////
# suma=0
# while True:
#     num=int(input("ingrese un numero , cero para salir:"))
#     if num==0:
#         break
#     suma+=num
#     print (suma)
# print(F"la suma total es {suma}")
# //////////////////////////////////////////////////////////////////////////////////////////
# pida al usuario el limite inferior y superior de un rango
# despues genere un numero al azar dentro de ese rango
# el segundo numero, no debe ser menor que el primero 
# pero debe darle la oportunidad al usuario de ingresar otro

# import random 
# print ("ingrese los numeros")
# n1=int(input("ingrese el primer numero"))
# n2=int(input("ingrese el primer numero"))

# numram=random.randint(n1, n2)             
# # .es para ver librerias
# print (numram)
# # //////////////////////////////////////////////////////////////

# import random 
# print ("ingrese los numeros")
# n1=int(input("ingrese el primer limite"))
# n2=int(input("ingrese el segundo limite"))
# numram=random.randint(n1, n2) 

# while n2<=n1:
#     print ("el numero debe ser mayor que el anterior")
#     n2=int(input("ingrese otro numero mayor que el anterior"))

# numram=random.randint(n1,n2)

# print (numram)
# //////////////////////////////////////////


# yo:

# import random 
# tries=3
# numram=random.randint(1,50)
# print ("ingrese un numero ")
# n1=int(input())
# while tries<=3:

#     if n1<numram:
#         print("el numero es mayor intenta denuevo")
#         tries=tries+1
#     else:
#         print ("el numero es menor intenta denuevo")
#         tries=tries+1
#     if numram==n1: 
#         break

# profe:

# intentos=5
# num=int(input())
# while numram!=num:
#     intentos-=1
#     if intentos==0
#         break
#     if num>numram:
#         print ("el numero a adivinar es menor")
#     else:
#         print ("el numero a a divinar es mayor")    
#         print(f"te quedan {intentos} intentos")   
#         num=int (input())

# print ("sos un genio adivinaste")

# if intentos==0:
#     print("perdiste")
# else:
#     print("sos un genio,adivinaste el numero")
# //////////////////////////////////////////////////////////////

# designe 2 peleadores solicitando sus nombres
# cadfa peleador tiene 50 hp debe mostraer la barra de energia  las peleas son por turnos 
# cada turno el peleador  ataca entre 3 y 15 
# existe posibilidad de ataque critico  del 20%
# gana el que quita todo el hp al rival
import time
import random

hp1=50
hp2=50
ultracounter=0
turno=random.randint(1,2)
j2atk=random.randint(3,15)
j2prob=random.randint(1,2) 
print ("welcome to code fighter")
print ("ingrese sus nombre j1" )
j1=input (())
print ("ingrese su nombre j2")
j2=input (())
print ("SELECT YOUR FIGHTER", (j1))
time.sleep(2)
print ( "Ryu",   " Ken"  ,  "Chun-Li" ,    "Birdie  5E. Honda" , "Blanka" ,  "Guile" , "Zangief")
j1char= input(())


print ("SELECT YOUR FIGHTER", (j2))
time.sleep(2)
print ( "Ryu",   "Ken"  ,  "Chun-Li" ,    "Birdie  5E. Honda" , "Blanka" ,  "Guile" , "Zangief")
j2char= input(())


print (j1char)
print("VS")
print(j2char)
time.sleep(2)
print("GET READY FOR BATTLEEEEEEEEEEEEEEEEEE")

while hp1>=0 and hp2 >=0:
    j1atk=random.randint(3,15)
    j2atk=random.randint(3,15)
    j1prob=random.randint(1,2)
    j2prob=random.randint(1,2)
    critical=random.randint(1,7)
    
    if turno==1:
        print(j1char ,"attacks")
        time.sleep(3)
     
        
    if  j1prob==1:
            print("hit!")
            
    if j1prob==2:
        print(j2char,"DODGED YOUR ATTACK")
    time.sleep(3)
    if critical==7:
            print("VISERAL HIT")
            j1atk*2
            hp2-=j1atk
            print(j2char)
            print("/"*hp2)
    else:
            
        hp2-=j1atk
           
        print(j1char)
        print("/"*hp1)


    if turno ==2:

        print(j2char,"attacks!")
        time.sleep(2)
        
        if  j2prob==2:
            print("hit!")
            
            if critical==7:
                print("VISERAL HIT")
                j2atk*2
                hp1-=j2atk
                print(j1char)
                print("/"*hp1)
            else:
                hp1-=j2atk
                
                print(j1char)
                print("/"*hp1)
    
    if j1prob==1:
        print(j2, "DODGED YOUR ATTACK")
            
if hp1<=0:
 
    j2atk=random.randint(3,15)
    j2prob=random.randint(1,2)
    if  j2prob==1:
        hp2-=j1atk
        ultracounter=ultracounter+1
        time.sleep(1)
else:
        print("//////////////////////////////////////////KO///////////////////////////////////")
        print ("////////////////////////////",(j2char), "WINS/////////////////////////////////////")
if ultracounter>=3:
        print(" ULTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") 
        



if hp2<=0:
    j1atk=random.randint(3,15)
    j1prob=random.randint(1,2)
    if  j1prob==1:
        hp1-=j2atk
        ultracounter=ultracounter+1
        time.sleep(1)
else:
        print("/////////////////////////////KO////////////////////////////////////////////////")
        print ("////////////////////////////",(j1char), "WINS/////////////////////////////////////")
if ultracounter>=3:
        print(" ULTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
     


 
 



     
 


# CREAR UN CAJERO AUTOMATICO 
# TENER EN CUENTA CAJAS DE BILLETES DE 5000 10000 Y 20000
# CADA CAJA  TIENE 30 BILLETES VERIFICAR SI EL MONTO SOLICITADO ESTA DISPONIBLE EN EL CAJERO
# VERIFICIAR SI MONTO SOLICITADO ES POSIBLE POR EL MULTIPLO DE LOS BILLETES DISPONIBLKES
# AL TERMNIAR CADA TRANSACCION DEBE MOSTRAR SALDO 

# intentos=3
# while intentos>0:
#     intentos-=1
#     color=input("ingrese un color: ")  

#     if color.lower()!="negro":
#         print("el color no es el requerido")
#     else:
#         print("el color es el requerido") 
#         break   

# la florida 20%, la pintana 30%, puente alto 25%, san joaquin 15%
# grupo familiar: 1=>2%, 2 a 4 => 3% 5 o mas =>4%
# preguntar al usuario en que comuna vive 
# preguntar con cuantas personas vive
# el arancel actual es de 200.000 por semestre
# basados en las respuestas del usuario y la info dada calcular descuento 


# clasificar segun categoria y precio 
# cat 1+200, cat 2+400, cat 3 +600
# precios: 1000 y menos;3%, entre 1001 y 5000 :5%, 5001 y mas 6%
#poner listadp de 3 productos por categoria  1 2 y 3 
# agregar los impuestos al precio , segun la cat y luego aplicar descuento al total de la boleta segun el monto 

