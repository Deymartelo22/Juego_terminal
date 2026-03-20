import random 
def daño_(min,max):
    daño = random.randint(min,max)
    if random.randint(1, 10) == 1:
        daño = daño * 2
    return daño

def estado (heroe, hp_h, hp_h_max, enemigo,hp_e, hp_e_max):
    bloques_h = int((hp_h / hp_h_max) * 10)
    vacios_h = 10 - bloques_h
    print(f"{heroe}: [{'#' * bloques_h}{'-' * vacios_h}] {hp_h} hp")

    bloques_e = int((hp_e / hp_e_max) * 10)
    vacios_e = 10 - bloques_e
    print(f"{enemigo}: [{'#' * bloques_e}{'-' * vacios_e}] {hp_e} hp")

def ganador (hp_h, hp_e):
    return hp_h <= 0 or hp_e <= 0


def turno_enemigo (hp_h):
    daño = daño_(15, 20)
    print(f"¡El enemigo ataca por {daño} de daño!") 
    hp_h = hp_h - daño
    return hp_h 

def turno_heroe (hp_h, hp_e, pociones):
    print("Elige que haras: (1)atacar, (2)curar, (3)habilidad especial")
    opcion = input("Elegiste: ")
    if opcion == "1":
        daño = daño_(10,25) 
        print(f"¡El heroe ataca por {daño} de daño!") 
        hp_e = hp_e - daño

    elif opcion == "2":
        if pociones > 0:
            pociones = pociones -1
            hp_h = hp_h + 20
            print(f"¡El heroe se cura y recuera 20 hp!")
        else:
            print("Sin pociones")
            
    elif opcion == "3":
        if random.randint(1, 2) == 1:
            daño = daño_(30,50)
            hp_e = hp_e -daño 
            print(f"¡La habilidad especial hace {daño} de daño!")
        else:
            print("¡La habilidad especial fallo!")

    return hp_e, pociones