#Importar librerias
from itertools import cycle

#Definicion de funciones
#Funcion que genera el digito verificador del dni
def digito_verificador(dni):
    reversed_digits = map(int, reversed(str(dni)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def datos():
    dni = int(input("Ingrese dni: "))
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    pais = input("Ingrese pais: ")
    ciudad = input("Ingrese ciudad: ")
    lista = [dni, nombre, edad, pais, ciudad]
    matriz.append(lista)
    return

def buscar(dni, num):
    i = 0
    j = 3
    for x  in range(len(matriz)):
        if matriz[x][i] == dni:
            if matriz[x][j] == "Argentina" and num == 0:
                print("Es Argentino.")
            if num == 0:
                print(matriz[x])
    return (x-1)

def imp_Certificado(palabra):
    print(f"Certificado de {palabra}")
    dni = int(input("Ingrese dni: "))
    x = buscar(dni= 1)
    #print(matriz[x])
    print(f"Nombre: {matriz[x][1]}")
    print(f"dni: {matriz[x][0]}")
    print(f"Edad: {matriz[x][2]}")
    print(f"Pais: {matriz[x][3]}")
    return


matriz = []
#Main
#Lista = [dni, nombre, edad, pais de nacimiento, ciudad de nacimiento]
op = "2"
while op != "5":
    print("1. Ingresar datos ")
    print("2. Buscar por dni ")
    print("3. Imprimir certificado ")
    print("4. ELIMINAR ")
    print("5. Salir")
    op = input("Ingrese opcion: ")
    if op == "1":
        datos()
    if op == "2":
        dni = int(input("Ingrese dni a buscar: "))
        buscar(dni= 0)
    if op == "3":
        print("1. Nacimiento")
        print("2. Estado Conyugal")
        print("3. Pertencia")
        opCertificado = input("ingrese opcion: ")
        if opCertificado == "1":
            certificado = "Nacimiento"
            imp_Certificado(certificado)
        elif opCertificado == "2":
            certificado = "Estado Conyugal"
            imp_Certificado(certificado)
        elif opCertificado == "3":
            certificado = "Pertenencia"
            imp_Certificado(certificado)
    if op == "4":
        dni= int(input("Ingrese dni a eliminar: "))
        x = buscar(dni= 1)
        matriz[x].pop()
        