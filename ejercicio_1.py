print("Ingresa 3 números distintos para validar cual es el menor")
num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))
num_3 = int(input("Ingresa el tercer númer: "))
if num_1 < num_2 < num_3:
    print(num_1)
elif num_2 < num_1 < num_3:
    print(num_2)
elif num_3 < num_1 < num_2:
    print(num_3)