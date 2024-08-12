
precio_pan_fresco=3.49
precio_pan_viejo= 3.49 * (60/100)

barras_pan_sold= int(input("Inserta el número de barras que vendiste:"))
print("El precio habitual de la barra de pan es de", precio_pan_fresco, "$")

print ("Por lo que pagarías:", barras_pan_sold*precio_pan_fresco, "$" )

print ("¿Esta cantidad de pan corresponde a barras que no son del día? (Si, no)")

barras_día_o_no=input ()

if (barras_día_o_no == "no"):
  print ("Tu valor seguiría siendo de:", barras_pan_sold*precio_pan_fresco, "$")

else:
  print ("El descuento que se le aplica a estas barras por no ser frescas es del 60% => Su valor sería de:")
  print (float(barras_pan_sold*precio_pan_viejo), "$")
