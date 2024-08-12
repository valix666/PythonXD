print ("Hello World :3")


saludo = "Hello World :3"
print (saludo)

print ("¿Cómo te llamas?")
nombre= input ()
print (f"Holi, {nombre}") 

print ("Inserta un número entero cualquiera:")
print (((3+2)/(2*5))**(2))


print ("¿Cuál fue tu número de horas trabajadas?")
horas_trabajadas= input ()
print ("¿Cuánto es el coste de tus horas trabajadas?")
coste_horas= input ()
print (f"Tu salario el día de hoy sería de {(int(horas_trabajadas)*int(coste_horas))}")

print ("Inserta un número (Solo valores enteros)")
n1= int (input ())
print ((n1) * (n1+1)/(2))

print("Calculo de tu IMC :3")
print ("Bienvenido")
print( "Inserta tu peso en kg")
W= input ()
print ("Inserta tu altura en metros")
H= input ()
IMC= (int(W)/float(H)**2)
print (f"Tu IMC es de {IMC}")


print("inserta un número entero como numerador/dividendo")
n= int(input ())
print("inserta un número entero como denominador/divisor")
m= int(input())
if m==0:
  print("# error: cociente no puede ser 0 :-#")
else:
  print ("el cociente de tu división es:" )
  c= int(n/m) 
  print(c)
  print ("el resto de tu división es:" )
  r= int(n%m)
  print (r)


print ("inserta tu monto a invertir")
i= input ()
print ("inserta el interés anual")
r= input ()
print ("inserte el número de años")
n= input ()
print ("tu capital obtenido con tu inversión es:")
print (int(i)*(int(r)/100)*int(n))

print ("¿Cuál es tu edad?")
edad= int(input ())
if edad < 18:
  print ("¡¿Qué chuchas haces aquí, si eres menor de edad?!")
else:
  print ("¡Eres mayor de edad! ¡Bienvenid@!")


print ("Ingresa tu contraseña:")
contraseña= str(input())

if contraseña == "Cu$hufli2022":
  print ("La contraseña ingresada es correcta")
else:
  print ("La contraseña ingresada es incorrecta")

numero= int(input("Ingresa un número entero:"))
if numero % 2==0:
  print ("El número ingresado es par")
else:
  print ("El número ingresado es impar")


print("Inserta la palabra que desees imprimir 10 veces:")
palabra_por_teclado= str(input())
i=0
for i in range(10):
  print (palabra_por_teclado)

print ("Inserta un número:")
numero_insertado= int(input())
print ("Ok :3")

print ("tu lista de números impares hasta" , numero_insertado, "es:")

lista_impares = []
for numero in range (1, numero_insertado+1,2):
  lista_impares.append(numero)
print ("Tu lista de números impares es:", lista_impares)



w_engranajes:112 
w_cilindros:75

engranajes_vendidos=int(input("inserte la cantidad de engranajes vendidos:"))

cilindros_vendidos=int(input("inserte la cantidad de cilindros vendidos"))

total= 112*engranajes_vendidos+ 75*cilindros_vendidos
print (total, "gr")


precio_pan_fresco=3.49
precio_pan_viejo= 3.49 * (60/100)

barras_pan_sold= int(input("Inserta el número de barras que vendiste:"))
print("El precio habitual de la barra de pan es de", precio_pan_fresco, "$")

print ("Por lo que pagarías:", barras_pan_sold*precio_pan_fresco, "$" )

print ("¿Esta cantidad de pan corresponde a barras que no son del día? (Si, no)")

barras_día_o_no=input ()

if (barras_día_o_no == "no"):
  print ("Tu valor seguiría siendo de:", barras_pan_sold*precio_pan_fresco, "$")
