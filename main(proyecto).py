repositorio_proyecto = ("https://github.com/InoveAlumnos/proyecto_inicial_python")

import random
import interfaz
from interfaz import dibujar 

def leer_palabra_secreta(palabras:list):
    palabra_random = random.choice(palabras)
    return palabra_random

def pedir_letra(letras_usadas:list):
    while True:
        pido_letra = str.lower(input("Ingrese una letra:"))
        
        if len(pido_letra) == 1:
            if pido_letra in letras_usadas:
                continue
            else:
                break
    return pido_letra

def verificar_letra(letra,palabra_secreta):
    if letra in palabra_secreta:
        return True
    else:
        return False
    
def validar_palabra(letras_usadas, palabra_secreta):
    lista_letras = ""
    for i in palabra_secreta:
        if i in letras_usadas:
            lista_letras += i
            continue
        else:
            print("Aun no se adivino la palabra oculta")
            break
    if palabra_secreta == lista_letras:
        return True
    else:
        return False


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de una lista.
    palabras = ["listas", 
                "bucles", 
                "variables",
                "archivos",
                "messi",
                "inove",
                "argentina",
                "talleres",
                "animales",
                "persona",
                "mundial"
        
                ]
    palabra_secreta = leer_palabra_secreta(palabras)
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)
        letras_usadas.append(letra)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')
