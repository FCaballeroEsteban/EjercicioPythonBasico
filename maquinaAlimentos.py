def maquina_alimentos():
    print("|-------------Maquina de alimentos-------------|")
    print("|a. Producto A-----------------------------$270|")
    print("|b. Producto B-----------------------------$340|")
    print("|c. Producto C-----------------------------$390|")
    print("|----------------------------------------------|")

    print("Escoja el producto que más te guste :3 ")
    
    a = 270
    b = 340
    c = 390

    op = input()

    if op == "a":
        print("Eligió producto A por valor de $270")
        print("RECUERDE: Esta máquina solo recibe monedas de $10, $50 o $100 pesos")
        print("Favor ingresar el dinero")
        vueltos(a)
    elif op == "b":
        print("Eligió producto B por valor de $340")
        print("RECUERDE: Esta máquina solo recibe monedas de $10, $50 o $100 pesos")
        print("Favor ingresar el dinero")
        vueltos(b)
    elif op == "c":
        print("Eligió producto C por valor de $390")
        print("RECUERDE: Esta máquina solo recibe monedas de $10, $50 o $100 pesos")
        print("Favor ingresar el dinero")
        vueltos(c)

def vueltos(i):
    moneda = 0
    while moneda < i:
        monedaval = int(input("Ingrese el valor de la moneda (10, 50, o 100): "))
        if monedaval == 10 or monedaval == 50 or monedaval == 100:
            moneda += monedaval
        else:
            print("El valor de la moneda no pudo ser leído, inténtelo de nuevo.")

    cambio = moneda - i
    while cambio > 0:
        if cambio >= 50:
            print("Su cambio es $50 ")
            cambio -= 50
        elif cambio < 50:
            print("Su cambio es $10")
            cambio -= 10
