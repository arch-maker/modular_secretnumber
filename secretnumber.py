import random
import json
import datetime

# Modo con posibilidad de 30 numeros, sin limite de intentos y con pistas.
def jugar_facil():
    secret = random.randint(1, 30)
    intentos = 0
    numeros_fallos = []
    score_list = lista_puntuacion()

    while True:
        num_usuario = int(input("Introduzca el numero secreto (Entre 1 y 30)"))
        intentos += 1

        if num_usuario == secret:
            score_list.append({"intentos": intentos, "date": str(datetime.datetime.now()), "jugador": usuario,
                               "fallos": numeros_fallos, "num_secreto": secret})

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("Enhorabuena acertaste el numero secreto: " + str(secret))
            print("Numero de intentoss: " + str(intentos))

            break

        elif num_usuario > secret:
            print("El numero introducido no es correcto... Prueba con un numero mas pequeño")

        elif num_usuario < secret:
            print("El numero introducido no es correcto... Prueba con un numero mas grande")

        numeros_fallos.append(num_usuario)
# Modo con posibilidad de 35 numeros, 6 intentos y sin pista alguna (el juego intenta desmoralizar)
def jugar_dificil():

    secret = random.randint(1, 35)
    intentos = 0
    numeros_fallos = []
    score_list = lista_puntuacion()

    while True:
        num_usuario = int(input("Introduzca el numero secreto (Entre 1 y 35)"))
        intentos += 1

        if intentos <= 5:
            if num_usuario == secret:
                score_list.append({"intentos": intentos, "date": str(datetime.datetime.now()), "jugador": usuario,
                                   "fallos": numeros_fallos, "num_secreto": secret})

                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                print("Enhorabuena acertaste el numero secreto: " + str(secret))
                print("Numero de intentoss: " + str(intentos))

                break

            elif num_usuario > secret:
                print("No das una :D")

            elif num_usuario < secret:
                print("No das una :D")

            numeros_fallos.append(num_usuario)

        elif intentos > 5:
            print("\nGAME OVER - NO TE QUEDAN MAS INTENTOS EN ESTA PARTIDA!")

            break

# Funcion con el registro total de puntuaciones.
def lista_puntuacion():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

# Funcion con el registros de las 3 mejores puntuaciones del juego.
def mejores_puntuaciones():
    score_list = lista_puntuacion()
    lista_ordenada = sorted(score_list, key=lambda s: s["intentos"])[:3]
    return lista_ordenada

# Menu del juego con operaciones y comunicacion con las distintas funciones. Cada vez que inicia pide registro usuario.
while True:
    print("1.- Jugar (Modo facil - Dificil)")
    print("2.- Ver puntuaciones en el juego.")
    print("3.- Ver las 3 mejores puntuaciones detalladas.")
    print("4.- Salir.")

    usuario = input("Introduce tu nombre de usuario: ")
    opcion = input("Seleccione la opcion para empezar: ")

    if opcion == "1":
        modo = input("Selecciona nivel de juego ([f] facil - [d] dificil): ")
        if modo == "facil" or modo == "f":
            jugar_facil()

        elif modo == "dificil" or modo == "d":
            jugar_dificil()

        else:
            print("Modo no disponible!")

    elif opcion == "2":
        for score_dict in lista_puntuacion():
            print(str(score_dict["intentos"]) + " intentos, con fecha: " + score_dict.get("date") + " usuario: " + score_dict.get("jugador"))

    elif opcion == "3":
        for score_dict in mejores_puntuaciones():
            puntuacion_txt = "El Jugador {0} tiene {1} intentos con fecha: {2}, nºsecreto: {3}, erroneos: {4}".format(score_dict.get("jugador"),
                                                                                                                      str(score_dict.get("intentos")),
                                                                                                                      score_dict.get("date"),
                                                                                                                      score_dict.get("num_secreto"),
                                                                                                                      score_dict.get("fallos"))
            print(puntuacion_txt)

    elif opcion == "4":
        print("Saliendo de la aplicacion....")

        break
    else:
        print ("OPCION INCORRECTA! INTRODUZCA LA OPCION CORRESPONDIENTE (1-4)")