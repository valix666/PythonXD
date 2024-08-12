print ("Inserta un número:")
numero_insertado= int(input())
print ("Ok :3")

print ("tu lista de números impares hasta" , numero_insertado, "es:")

lista_impares = []
for numero in range (1, numero_insertado+1,2):
  lista_impares.append(numero)
print ("Tu lista de números impares es:", lista_impares)
