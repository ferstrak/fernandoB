
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
# import time
# import random

# hp1=50
# hp2=50
# ultracounter=0
# turno=random.randint(1,2)
# j2atk=random.randint(3,15)
# j2prob=random.randint(1,2) 
# print ("welcome to code fighter")
# print ("ingrese sus nombre j1" )
# j1=input (())
# print ("ingrese su nombre j2")
# j2=input (())
# print ("SELECT YOUR FIGHTER", (j1))
# time.sleep(2)
# print ( "Ryu",   " Ken"  ,  "Chun-Li" ,    "Birdie  5E. Honda" , "Blanka" ,  "Guile" , "Zangief")
# j1char= input(())


# print ("SELECT YOUR FIGHTER", (j2))
# time.sleep(2)
# print ( "Ryu",   "Ken"  ,  "Chun-Li" ,    "Birdie  5E. Honda" , "Blanka" ,  "Guile" , "Zangief")
# j2char= input(())


# print (j1char)
# print("VS")
# print(j2char)
# time.sleep(2)
# print("GET READY FOR BATTLEEEEEEEEEEEEEEEEEE")

# while hp1>=0 and hp2 >=0:
#     j1atk=random.randint(3,15)
#     j2atk=random.randint(3,15)
#     j1prob=random.randint(1,2)
#     j2prob=random.randint(1,2)
#     critical=random.randint(1,7)
    
#     if turno==1:
#         print(j1char ,"attacks")
#         time.sleep(3)
     
        
#     if  j1prob==1:
#             print("hit!")
            
#     if j1prob==2:
#         print(j2char,"DODGED YOUR ATTACK")
#     time.sleep(3)
#     if critical==7:
#             print("VISERAL HIT")
#             j1atk*2
#             hp2-=j1atk
#             print(j2char)
#             print("/"*hp2)
#     else:
            
#         hp2-=j1atk
           
#         print(j1char)
#         print("/"*hp1)


#     if turno ==2:

#         print(j2char,"attacks!")
#         time.sleep(2)
        
#         if  j2prob==2:
#             print("hit!")
            
#             if critical==7:
#                 print("VISERAL HIT")
#                 j2atk*2
#                 hp1-=j2atk
#                 print(j1char)
#                 print("/"*hp1)
#             else:
#                 hp1-=j2atk
                
#                 print(j1char)
#                 print("/"*hp1)
    
#     if j1prob==1:
#         print(j2, "DODGED YOUR ATTACK")
            
# if hp1<=0:
 
#     j2atk=random.randint(3,15)
#     j2prob=random.randint(1,2)
#     if  j2prob==1:
#         hp2-=j1atk
#         ultracounter=ultracounter+1
#         time.sleep(1)
# else:
#         print("//////////////////////////////////////////KO///////////////////////////////////")
#         print ("////////////////////////////",(j2char), "WINS/////////////////////////////////////")
# if ultracounter>=3:
#         print(" ULTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") 
        



# if hp2<=0:
#     j1atk=random.randint(3,15)
#     j1prob=random.randint(1,2)
#     if  j1prob==1:
#         hp1-=j2atk
#         ultracounter=ultracounter+1
#         time.sleep(1)
# else:
#         print("/////////////////////////////KO////////////////////////////////////////////////")
#         print ("////////////////////////////",(j1char), "WINS/////////////////////////////////////")
# if ultracounter>=3:
#         print(" ULTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
     


 
 


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     
 


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

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# calcular el puntaje de credito 
# calcular cuanto credito tiene una persona
# en cierta entidad financiera considear:

# cantidad de ingresos

# nivel educacional

# nacionalidad

# cantidad de ingresos:
# 500.000 a 1.000.000: 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.000 o mas: 1.000.000

# nivel educacional:

# basico: x1, 
# medio: x1.3
# superior:1.5

# nacioinalidad:
# chilena:+300.000
# extranjero:+0


# credito=0

# print("Bienvenido a su simulación de crédito bancario")
# ing= int(input("""Seleccione su rango de ingresos:
#           1.- $500.000 a 1.000.000
#           2.- $1.000.000 a $1.500.000
#           3.- $1.500.000 o más
          
#           """))

# if ing==1:
#     credito+=300000
# elif ing==2:
#     credito+=650000
# elif ing==3:
#     credito+=1000000
# else:
#     print("Ingrese una opción válida")

# ne= int(input("""Seleccione su nivel educacional:
#           1.- Básica
#           2.- Media
#           3.- Superior
          
#           """))
# if ne==1:
#     credito=credito
# elif ne==2:
#     credito=credito*1.3
# elif ne==3:
#     credito=credito*1.5
# else:
#     print("Ingrese una opción válida")

# nacio=int(input("""Seleccione su nacionalidad:
#           1.- Chilena
#           2.- Extranjera
          
#           """))

# if nacio==1:
#     credito+=300000
# elif nacio==2:
#     credito=credito
# else:
#     print("Ingrese una opción válida")










# /////////////////////////////////////////////////////////////////////////

# pedir dia y mes de nacimiento y mostrar el signo zodiacal 
# //////////////////////////////////////////////////////////////////////////////////

# pida al iusuario 2 digitos verificando si el segundo es mayor
# genere un numero aleatorio entre esos digitos 
# imprima el numero de veces que salio ese numero por medio del siguiente simbolo ▄
# import random

# print ("ingrese 2 numeros")

# print ("ingrese numero 1")
# n1=int(input())
# print ("ingrese numero 2")
# n2=int(input())

# while n1>n2:
#     print ("el numero 2 no puede ser mayor que el numero 1")
#     n2=int(input("numero 2:"))


# num=random.randint(n1,n2)  

# print("▄"*num)

# //////////////////////////////////////////////////////////////////////////////////////////////////

# crear un programa que pida la cantidad de ramos 
# luego pida el promedio por cada materia 
# basados en su promedio final
#  aplicar puntaje de beneficios
# 4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0: 800
# agregar puntaje segun carrera
# tecnico: +60, ingenieria: +40, diplomado:+20
# import time
# print("ingrese cantidad de ramos")
# nramos=int(input())
# for i in range (nramos):
#     nota=float(input("ingrese el promedio de cada ramo"))
#     total= nota+1

# promedio=total/nramos

# print ("su promedio es", round(promedio),1)

# print ("calculando beneficios")
# time.sleep (3)

# beneficio=0

# if promedio(4.5,5.0):
#     beneficio+=300
# elif promedio(5.1,6.0):
#     beneficio+=500
# elif promedio(6.1,7.0):
#     beneficio+=800
# print ("su beneficio es", beneficio)

# print ("""ingrese su carrera
#        1 tecnico
#        2 ingenieria
#        3 diplomado""""")
# carrera=input(())

# if carrera==1:
#     beneficio+=

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FUNCIONES

# def suma():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print ("la suma es", n1+n2)
# def resta():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print ("la resta es", n1-n2)
# def multi():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print ("la multiplicacion es", n1*n2)
# def divi():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     try:
#         resulta=n1/n2
#         print("la division es", resulta)
#     except ZeroDivisionError:
#         print ("la división por cero no esta permitida")
# def calcu():
#     while True:
#         op=int(input ('''seleccione una opcion:
#                     1. suma
#                     2. resta
#                     3. multiplicación
#                     4. division
#                     5. salir
                      
#                       ''' 
                     
#                    ))
#         match op:
#             case 1:
#                 print("suma")
#                 suma()

#             case 2:
#                 print("resta")
                
#                 resta()
            
#             case 3:
#                 print("multi")
                
#                 multi()
                                                
#             case 4:
#                 print("divi")
               
#                 divi() 

#             case 5:
#                 print ("saliendo")   
#                 break                                   
#             case _:
#                 print ("saliendo")  

# calcu() 
                                               
# ctrl alt mas flechas seleccionas varias lineas y shift + alt volver tabs  case_: opcion default    seleccionar todo y poner "" ahorra tiempo al poner texto print  repasar while true y false

# realizar un programamque inluya match y llame a otras 3 funciones estas funciones deben incluir if, if else, for y/o while y el programa debe ser recursivo

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def menu_tarea():
#     while True:
#         print('''
#             seleccione una opción
#             1 numero al azar
#             2 calcular arancel 
#             3 salir
#                         ''')
#         op=int(input())
#         match op:
#             case 1:
#                 azarN()
#             case 2:
#                 arancel()
#             case 3:
#                 break
#             case _:                                                                     #para todo lo no mencionado#   
#                 print ("opción invalida") 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# crear un menu de carrito con las siguientes opciones
# ingresqar nombre de ususario que sera mostrado en la boleta con un saludo 
# comprar y poner productos para comprar con su precio correspondiente
# sacar boleta calcular precio neto y el precio mas iva y mostrar totales
# salir

# consideraciones:
# por lo menos 3 productos
# no hay limite de compra 
# se puede salir en cualquier momento
# los montos de los productos son fijos
  


    
# def multi(): 
#     global multic
    
#     print("elegiste multitool por 15000 units")
#     n+=15000
   
#     multic+=1
   
# def cat():  
#     global catc
#     print("elegiste cataplasm por 20000 units")
#     n+=20000
#     catc+=1
  
# def heal():
#     global healc   
#     print("elegiste healkit por 8000 units")
#     n+=8000
#     healc+=1


    
# def compra():

#     while True: 
       
#         n=0 

#         print ("bienvenido a su carrito porfavor ingrese su nombre")
#         nom=input(())
#         print ('''productos disponibles
#             1. multi tool 15000 unit)
#             2. cataplasm 20000 unit)
#             3. heal kit 8000 unit
#             4. salir''')
        
        
#         op=int(input())

            
#         match op:
#             case 1:
#                 multi()
#             case 2:
#                 cat()   
#             case 3:
#                 heal()
                                                        
#             case 4:
#                 print("saliendo..")
#                 break
#             case _:
#                 print("opción invalida")

#         print("lleva", multic ,"multitools",catc , healc , "healkits" )

#         print("el total de su compra es",n) 


# # ///////////////////////////////////////////////////////////////////////////
# # promedios por cantidad de alumnos

# pedir cantidad de alumnos
# pedir notas por cada alumno
# promediar a cada alumno
# y mostrar si aprueba o no aprueba
# bonus: mostrar promedios de todos los almunos






#   ////////////////////////////////////////////////////////////////////////////////              
               
#  dato extra del profe:               
# # def suma_ret():
# #     n1=int(input("ingrese un numero"))
# #     n2=int(input("ingrese otro numero"))
# #     return n1+n2

# # nume=suma_ret()
# # for i in range (nume):
# #     print("hola")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# for:
# perros de caza
# pida al usuario la cantidad de perros
# muestr cual es la cuota minima de conejos
# luego consulte cuantos conejos trajo
# si elperro trajo la camtiodad minima cumplio la cuota sino se queda sin Filete 
# mostrar resumen de perro que cumplieron y los que no
# cantmin=3
# total=0
# perro=1
# perroS=0
# perroN=0
# cant=int(input("ingrese un numero de perros"))
# print("hay un total de", cant , "perros")
# print ("la cuota minima de cinejos es 5")
# print ("cuantos conejos trajo cada perro")

# for i in range (cant):
#     int(input("cuantos conejos cazo el perro", perro))
#     if cantmin>=3:
#         print("cumple con la cuota")
#         perro+=1
#         perroS+=1
#     elif cantmin<3:
#         print("no cumple con la cuota")
#         perro+=1
#         perroN+=1

# print ("los que cumplieron son un total de", perroS , "los que no", perroN)



# # profe:

# import random 
# while True:
#     try:
#         cant=int(input("ingrese un numero de perros"))
#         break
#     except Exception:
#         print("solo se aceptan numeros enteros")
# cuota=3
# cumple=0


# for i in range(cant):
#     con=random.randint(0,5)
#     print(f"el perro {i+1} trajo {con} conejos")
#     if con>=cuota:
#         print("el perro gana filete")
#         cumple+=1
#     else:
#         print("se queda sin carne")
        

# print(f"la cantidad de perro que cumplieron es {cumple}")
# print(f"la cantidad de perro que cumplieron es {cant-cumple}")

# quiere pasar el ramo
# pregunte la cantidad de rojos en el curso
# los talleres que hay en el semestre son 4
# por cada taller asistido obtiene 0.3 decimas
# si el alumno tiene mas de 1 punto
# tiene la bendicion del profe
# sino no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# muestre si aprueba o reprueba

# import random
# while True:
#     try:
        
#         cant=int(input("ingrese el numero de rojos en el curso"))
#         break
#     except Exception:
#         print("solo se aceptan numeros enteros")
# extra=0


# for i in range(cant):
   
#     print("cuantos talleres asistio")
#     con=random.randint(0,5)
    
#     print(f"el estudiante {i+1} asistio a {con} talleres")

#     if con==0:
#         print("no asistio a ningun taller")
#     if con==1:
#         extra+=0.3
#     if con==2:
#         extra+=0.3
        
#     if con==3:
#         extra+=0.3
        
#     if con==4:
#         extra+=0.3
       
#     if con>4 or con<1:
#         print("no es valido")
        
#    # ver random choice como funciona. es con opciones textuales no numerossssssssssssssssssssssssssssssssss

# if extra>1.0:
#     print ("tiene la bendicion del profe")
# elif extra<1.0:
#     print ("no tiene la bendicion del profe")

# print ("ingrese su nota final")
# nota=float(input())

# if (nota+extra)>5.0:
#     print("usted aprobo")
# else:
#     print("usted no aprobo")

# profe:
# rojos=int(input("diga la cant de rojos: "))

# talleres=4
# tDecimas=0
# for r in range(rojos):
#     for t in range(talleres):
#      asist=input(f"asistio al taller numero {t+1}? 1.- si,  2.- no")
#      if asist.lower()=="si":
#         tDecimas+=0.3
#     if tDecimas>=1:
#        print("tiene la bendicion del profe")
#     else:
#        print("nada mas que hacer")
#     nf=float(input("ingrese su nota final"))
#     nf+=tDecimas
# if tDecimas>=1:
#    print(f"su nota final es {nf}")
# if nf>=4:
#       print("el alumno aprobo")
# elif nf<4:
#        print("el alumno aprobo")
       
# //////////////////////////////////repasar match, case y try para menus///////////////////////////////////

# lavado de autos 
# crear un menu para lavar auto
# 2,- cursar pago del lavado
# 3,- ver ventas diarias
# 4,- salir
# el lavado tiene 3 nuiveles
# 1 ful 15000 2 standard 10000 3 basico 7000
# al mostrar las ventas diarias debe mostrar la cantidad de autos que han ingresado y el monto total recaudado
# mostrar el monto total pagado

# import time
# print ("bienvenido a lavado de autos donde el tio wea ")
# time.sleep(1)
# while True:
#     try:
#         print ("¿que deseea realizar?")
#         time.sleep(1)
#         serv=int(input('''1 full 15000
#                 2 standard 10000
#                 3 basico 7000'''))
#         break
#     except Exception:
#        print("solo se aceptan numeros enteros dentro del rango")
# for i in range (serv):

# //////////////////////////////////////////////////////////////////////////////////////////////

# actividad 2.5.3

# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:

# 1. Pago de Tarjeta de Crédito:

# a. El usuario comienza con una deuda de $100.000

# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.

# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.

# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.

# e. Al pagar el sistema debe descontar de la deuda total

# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.



# 2. Simulación de Compras:

# a. El usuario puede simular realizar un número ilimitado de compras.

# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.

# c. Se verifica que el monto de la compra sea mayor o igual a cero.

# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.




# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar considerar:



# 1. Manejo de Errores:

# a. Se utilizan bloques try y except para manejar posibles errores al

# ingresar datos, validar valores no numéricos y errores inesperados.

# 2.b. Se debe programar mensajes de error específicos para guiar al
# usuario sobre posibles problemas


# yo
# montotaldeuda=100.000
# import time
# print ("bienvenido al programa de pago de tarjetas. Ingrese su numero de rut")
# rut=int(input())
# print ("tras revisar su cuenta debe un monto de 100.000")
# time.sleep(1)
# print ("cuanto desea pagar?")
# montopagar=float(input())
# if montopagar<0:
#     print("ingrese un numero valido")
# if montopagar>=montotaldeuda:
#     print ("has superado el saldo actual de la tarjeta.")

# elif montopagar<montotaldeuda:
#     print("el saldo actual de la tarjeta es", montotaldeuda-montopagar)




    # ///////////////////////////////////////////////////////////////////////////////////////////++



  



# profe


# deuda=100000

# while True:
#     op=int(input('''
# seleccione una opción
#      1.- pago
#      2.- compra            
#      3.- salir            
# '''))
    
#     match op:
#         case 1:
#             print(f"la deuda actual es {deuda}")
#             while True:
#                 try:
#                     pago=int(input("ingrese el monto a pagar"))
#                     break
#                 except Exception:
#                     print("solo se a admiten numeros enteros")
#             if pago>0 and pago<=deuda:
#                 deuda=deuda-pago

#             else:
#                 print(f"el pago debe ser mayor a cero y no exceder {deuda}")        

            

#         case 2:
#             print("comprando")
#             monto=int(input("ingrese el monto de la compra: "))
#             deuda+=monto
#             print(f"la deuda actual es {deuda}")


#         case 3:
#             print ("saliendo...")
#             break


#         case _:
#             print("opcion invalida")
    
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).

# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
#  (validar usando for y while) y lo guardará en una variable llamada “correo”.

# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”

# Finalmente cerrar sesión, volverá al menú principal.

# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.

# Recuerde utilizar try Exception en caso de ser necesario


usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
usertrycount=0
userpasswdtrycount=0
while True:
    op=int(input ('''
                  selecciona una opcion
                  1.- iniciar sesión
                  2.- registrar usuario 
                  3.- salir
                  '''))
    match op:
        case 1:
            print ("ingrese usuario")
            usertry=input (())
            if (usertry!=usuario1)(usertry!=usuario2) and (usertry!=usuario3):
               print("usuario no encontrado")
               userpasswdtrycount+=1
            else:
                print(" usuario encontrado")

            while
            print("ingrese contraseña")
            userpasswdtry=input (())
            if (userpasswdtry!=contrasena1)(userpasswdtry!=contrasena2) and (userpasswdtry!=contrasena3):
               print("contraseña incorrecta")
               userpasswdtrycount+=1
            else:
                print("bienvenido")
        case 2:
        case 3:
            break
        case _:
            print("opción invalida")
    # ///////////////////////////////////////////////////////////////////////////////////////////


usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
usertrycount=0
userpasswdtrycount=0
while True:
    op=int(input ('''
                  selecciona una opcion
                  1.- iniciar sesión
                  2.- registrar usuario 
                  3.- salir
                  '''))
    match op:
        case 1:
        case 1:
        case 1:
        case 1:

usar listas






