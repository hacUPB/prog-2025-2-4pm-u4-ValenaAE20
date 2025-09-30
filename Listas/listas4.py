
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas =[1200, 1200, 5000, 800, 800, 600]
posiciones_x = [-2, 2, 0, -2, 2, -6]

#Cálculo de centro de masa 
masa_total = 0
momento_total = 0

# for i in range(len(masas)):
#
#
for m, p in zip(masas, posiciones_x):
    masa_total += m
    momento_total += m*p

centro_masa_X = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m")

#Imprimir cuánta masa hay en cada componente del avión
for comp, masa in zip(componentes, masas):
    print(f"{comp:20} --> {masa:10} Kg")
    