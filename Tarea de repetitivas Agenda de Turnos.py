Lunes = 0
Lunes1 = "libre"
Lunes2 = "libre"
Lunes3 = "libre"
Lunes4 = ""
Martes = 0
Martes1 = "libre"
Martes2 = "libre"
Martes3 = "libre"
Activo = True
while Activo == True:
    Accion = input("Que desea hacer?\n" \
    "1.Reservar turno\n" \
    "2.Cancelar turno\n" \
    "3.Ver Agenda del dia\n" \
    "4.Ver resumen general\n" \
    "5.Cerrar Sistema\n")
    match Accion:
        case "1":
            Accion2 = input("Indique el dia en el cual quiere reservar turno:\n" \
            "1.Lunes\n" \
            "2.Martes\n")
            if Accion2 == "1":
                NombreDelPaciente = input("cual es tu nombre? ").capitalize()
                if NombreDelPaciente.isalpha():
                    if NombreDelPaciente in [Lunes1,Lunes2,Lunes3,Lunes4]:
                        print("esta persona ya tiene un turno ese dia")
                    elif Lunes >= 4:
                        print("todos los turnos estan ocupados")
                    else:
                        if Lunes1 == "libre":
                            Lunes1 = NombreDelPaciente
                            Lunes += 1
                        elif Lunes2 == "libre":
                            Lunes2 = NombreDelPaciente
                            Lunes += 1
                        elif Lunes3 == "libre":
                            Lunes3 = NombreDelPaciente
                            Lunes += 1
                        elif Lunes4 == "libre":
                            Lunes4 = NombreDelPaciente
                            Lunes += 1
                else:
                    print("solo te permiten letras")
            elif Accion2 == "2":
                NombreDelPaciente = input("cual es tu nombre? ").capitalize()
                if NombreDelPaciente.isalpha():
                    if NombreDelPaciente in [Martes1,Martes2,Martes3]:
                        print("esta persona ya tiene un turno ese dia")
                    elif Martes >= 3:
                        print("todos los turnos estan ocupados")
                    else:
                        if Martes1 == "libre":
                            Martes1 = NombreDelPaciente
                            Martes += 1
                        elif Martes2 == "libre":
                            Martes2 = NombreDelPaciente
                            Martes += 1
                        elif Martes3 == "libre":
                            Martes3 = NombreDelPaciente
                            Martes += 1
                else:
                    print("solo te permiten letras")
            else:
                print("Numero no valido")
        case "2":
            NombreDelPaciente = input("Nombre de la persona que posee el turno:\n").capitalize()
            if Lunes1 == NombreDelPaciente:
                Lunes1 = "libre"
                Lunes -= 1
            elif Lunes2 == NombreDelPaciente:
                Lunes2 = "libre"
                Lunes -= 1
            elif Lunes3 == NombreDelPaciente:
                Lunes3 = "libre"
                Lunes -= 1
            elif Lunes4 == NombreDelPaciente:
                Lunes4 = "libre"
                Lunes -= 1
            elif Martes1 == NombreDelPaciente:
                Martes1 = "libre"
                Martes -= 1
            elif Martes2 == NombreDelPaciente:
                Martes2 = "libre"
                Martes -= 1
            elif Martes3 == NombreDelPaciente:
                Martes3 = "libre"
                Martes -= 1
            else:
                print("Nombre no encontrado en ningun dia.")
        case "3":
            print ("turnos para el Lunes...")
            print("Turno 1: " + Lunes1)
            print("Turno 2: " + Lunes2)
            print("Turno 3: " + Lunes3)
            print("Turno 4: " + Lunes4)
            print ("turnos para el Martes...")
            print("Turno 1: " + Martes1)
            print("Turno 2: " + Martes2)
            print("Turno 3: " + Martes3)
        case "4":
            print(f"Turnos del Lunes:{Lunes}")
            print(f"el lunes tiene {4-Lunes} turnos disponibles")
            print(f"Turnos del Martes:{Martes}")
            print(f"el lunes tiene {3-Martes} turnos disponibles")
            if Lunes > Martes:
                print("el lunes tiene más turnos ocupados que el martes")
            elif Martes > Lunes:
                print("el martes tiene más turnos ocupados que el lunes")
            else:
                print("ambos dias tienen la misma cantidad de turnos ocupados")
        case "5":
            print("adios")
            Activo = False