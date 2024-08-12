
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
