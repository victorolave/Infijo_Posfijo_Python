import Evaluador
import os

expresion_infija = ""

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("_________________________________________")
    print("______________   Menu    ________________")
    print("\t1 - Ingresar Expresion")
    print("\t2 - Mostrar expresion en forma Infija")
    print("\t3 - Mostrar expresion en forma Postfija")
    print("\t4 - salir")
    print("_________________________________________")


def convertir(expresion_infija):
    expresion_infija = list(expresion_infija.upper())
    expresion_postfija = []
    return Evaluador.evaluar(expresion_infija, 100, expresion_postfija)


while True:
    # Mostramos el menu
    menu()

    # Solicitamos una opción al usuario
    opcion_menu = input("Digite una opción >> ")

    if opcion_menu == "1":
        expresion_infija = input("Digite la expresion: ")
        print("Expresion Guardada!")
    elif opcion_menu == "2":
        if expresion_infija == "":
            print("No ha ingresado una expresion")
        else:
            print("La expresion en su forma infija es: ", expresion_infija)
    elif opcion_menu == "3":
         if expresion_infija == "":
             print("No ha ingresado una expresion")
         else:
            print(convertir(expresion_infija))

    elif opcion_menu == "9":
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")












