
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


         
        
 





   




