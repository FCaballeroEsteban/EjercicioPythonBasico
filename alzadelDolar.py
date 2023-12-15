alza = []
dolarV = []

diaN = int (input(f"Ingrese el numero de dias")) 
print(f"Ingrese el valor del dolar del dia ")
for i in range(1,diaN+1):
    precioDOlar = int(input(f"Dia{i}:"))
    dolarV.append(precioDOlar)

for i in range(diaN-1):
    elAlza_1 = dolarV[i+1]-dolarV[i]
    alza.append(elAlza_1)

maxalza = max(alza)
print(f"La mayor alza fue de {maxalza}.")

