from funciones import *
hp_h = 100 
hp_e = 120
pociones = 3

while not ganador (hp_h, hp_e):
    estado("Heroe", hp_h, 100, "Enemigo", hp_e, 120)
    hp_e, pociones = turno_heroe(hp_h, hp_e, pociones)
    hp_h = turno_enemigo(hp_h)


if hp_h > 0:
    print("¡Victoria!")
else:    
    print(" Game over...")
