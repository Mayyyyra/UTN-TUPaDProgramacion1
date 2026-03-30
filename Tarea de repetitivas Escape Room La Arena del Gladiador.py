VidaDelJugador = 100
VidaDelEnemigo = 100
DañoBase = 15
DañoBaseDelEnemigo = 12
PoscionesDeVida = 3
Activo = True
TurnoEnemigo = False
nombre = ""
while nombre == "":
    nombre = input("nombre del jugador: ")
    if not nombre.isalpha():
        nombre = ""
        print("Error: Solo se permiten letras")
while VidaDelEnemigo > 0 and VidaDelJugador > 0:
    print(f"tú vida: {VidaDelJugador}")
    print(f"vida del enemigo: {VidaDelEnemigo}")
    while TurnoEnemigo == False:
        Accion1 = (input("1. Ataque Pesado\n" \
        "2. Ráfaga Veloz\n" \
        "3. Curar\n"))
        if Accion1.isdigit():
            Accion1 = int(Accion1)
        if Accion1 == 1:
            Accion1 = ""
            if 20 > VidaDelEnemigo:
                print("golpe critico!")
                VidaDelEnemigo -= DañoBase * 1.5
                TurnoEnemigo = True
            else:
                VidaDelEnemigo -= DañoBase
                TurnoEnemigo = True
        elif Accion1 == 2:
            for att in range(3):
                VidaDelEnemigo -= 5
            print(f"el jugador conecto 3 ataques por 5 de daño cada uno")
            TurnoEnemigo = True
            Accion1 = ""
        elif Accion1 == 3:
            Accion1 = ""
            if PoscionesDeVida > 0:
                VidaDelJugador += 30
                PoscionesDeVida -= 1
                TurnoEnemigo = True
            else:
                print("no te quedan posciones")
                TurnoEnemigo = True
        else:
            Accion1 = ""
    while TurnoEnemigo == True:
        VidaDelJugador -= 12
        print("el enemigo te atacó por 12 puntos de vida")
        TurnoEnemigo = False
        print("_____________________________________")
if 0 > VidaDelEnemigo:
    print("Ganaste!")
elif 0 > VidaDelJugador:
    print("Perdiste")