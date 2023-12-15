import random
numeros_Random = [random.randint(0,10) for i in range(10)]
print(f"LA LISTA ORIGINAL ES: ", numeros_Random)
numeromenor_mayor = sorted(numeros_Random)
print(f"LA LISTA DE FORMA ASCENDENTE ES: " , numeromenor_mayor)
numeromayor_menor = sorted(numeros_Random , reverse=True)
print(f"LA LISTA DE FORMA DESCENDENTE ES: " , numeromayor_menor) 