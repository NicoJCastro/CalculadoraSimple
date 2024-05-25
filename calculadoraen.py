
#Calculadora
def calculadora():
    print("Bienvenido a la Super Calculadora de Nico")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Ingrese la operación a realizar: "))
    if opcion == 1:
        n1 = float(input("Primer número:"))
        n2 = float(input("Segundo número:"))
        print("Resultado de la suma:", n1 +n2)
    if opcion == 2:
        n1 = float(input("Primer número:"))
        n2 = float(input("Segundo número:"))
        print("Resultado de la resta:", n1 - n2)
    if opcion == 3:
        n1 = float(input("Primer número:"))
        n2 = float(input("Segundo número:"))
        print("Resultado de la multiplicación:", n1 * n2)
    if opcion == 4:
        n1 = float(input("Primer número:"))
        n2 = float(input("Segundo número:"))
        print("Resultado de la división:", n1 / n2)
    if opcion == 5:
        print("Hasta luego!")       
        
calculadora()

