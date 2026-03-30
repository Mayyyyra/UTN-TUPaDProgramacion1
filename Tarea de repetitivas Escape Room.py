energia = 100
tiempo = 12
cerraduras_abiertas = 0
antispam = 0
alarma = False
codigo_parcial = ""
codigo = "KSAodasf"
nombre = ""
posicionCodigo = 0
Accion1 = ""
while nombre == "":
    nombre = input("nombre del agente: ")
    if not nombre.isalpha():
        nombre = ""
        print("solo letras")
while energia > 0 and tiempo > 0 and 3 > cerraduras_abiertas and Accion1 == "" and alarma == False:
    print("1.Forzar cerradura (costo: -20 energía, -2 tiempo)\n" \
    "2.Hackear Panel (costo: -10 energía, -3 tiempo)\n" \
    "3.Descansar (costo: +15 energía (máx 100), -1 de tiempo")
    Accion1 = input("...")
    match Accion1:
        case "1":
            if 40 > energia:
                print("hay riezgo de que se encienda la alarma si lo haces ahora, proceder?")
                r = input("s/n\n").lower()
                match r:
                    case "s":
                        energia -= 20
                        tiempo -= 2
                        antispam += 1
                        Accion1 = ""
                        cerraduras_abiertas += 1
                        NumeroAlAzar = int(input("elije un numero del 1 al 3"))
                        if NumeroAlAzar == 3:
                            alarma = True
                            cerraduras_abiertas -= 1
                        if antispam >= 3:
                            alarma = True
                            cerraduras_abiertas -= 1
                    case "n":
                        print("entendido")
                    case _:
                        print("?")
            elif alarma == False:
                energia -= 20
                tiempo -= 2
                antispam += 1
                Accion1 = ""
                cerraduras_abiertas += 1
                print(antispam)
                if antispam >= 3:
                    alarma = True
        case "2":
            energia -= 10
            tiempo -= 3
            antispam = 0
            Accion1 = ""
            
            for x in range(4):
                if posicionCodigo < len(codigo):
                    codigo_parcial += codigo[posicionCodigo]
                    posicionCodigo += 1
                    if 8 <= len(codigo_parcial):
                        cerraduras_abiertas += 1
                        posicionCodigo = 0
                        codigo_parcial = ""
        case "3":
            if alarma == False:
                energia += 15
                if (energia > 100):
                    energia = 100
                tiempo -= 1
                antispam = 0
                Accion1 = ""
            else:
                energia -= 10
                antispam = 0
                if (0 > energia):
                    energia = 100
        case _:
            Accion1 = ""
            print(f"energia:{energia}")
            print(f"tiempo:{tiempo}")
            print(f"anti spam: {antispam}")
            print(f"codigo parcial: {codigo_parcial}")
            print(f"Cerraduras abiertas: {cerraduras_abiertas}")
if cerraduras_abiertas >= 3:
    print("ganaste")
elif alarma == True:
    print("encendiste la alarma,perdiste")
else:
    if 0 >= energia or 0 >= tiempo:
        print("perdiste")