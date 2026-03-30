UsuarioCorrecto = "Martinez"
ContraseñaCorrecta = "hola123"
Activo = True
bloqueado = False
intentos = 0
Accion = ""
ContraseñaNueva = ""
while bloqueado == False:
    Usuario = input("introduzca su Usuario: ")
    Contraseña = input("introduzca su conrtraseña: ")
    intentos += 1
    if Usuario != UsuarioCorrecto or Contraseña != ContraseñaCorrecta:
        print(f"credenciales incorrrectas")
        if intentos > 3:
            print("cuenta bloqueada")
            bloqueado = True
    else:
        print("bienvenido")
        while Activo == True:
        
            while Accion == "":
                Accion = (input("que desea ver?\n" \
                    "1: ver estado de la inscripción\n" \
                    "2:Cambiar la clave\n" \
                    "3:Mostrar mensaje motivacional\n" \
                    "4:Salir\n"))
                if Accion.isdigit() and 5 > int(Accion):
                    Accion = int(Accion)
                else:
                    print("accion no valida")
                    Accion = ""
            match Accion:
                case 1:
                    print("Estado de la inscripcion:Inscripto")
                case 2:
                    while ContraseñaNueva == "":
                        Contraseña = input("Para cambiar la contraseña primero escriba la actual: ")
                        if Contraseña == ContraseñaCorrecta:
                            ContraseñaNueva = input("Nueva contraseña: ")
                            if 6 > len(ContraseñaNueva):
                                print("debe tener como minimo 6 caracteres")
                                ContraseñaNueva = ""
                            else:
                                ContraseñaCorrecta = ContraseñaNueva
                                print("contraseña restablecida")
                                ContraseñaNueva = ""  # Reset for next time
                        else:
                            print("contraseña incorrecta")
                case 3:
                      print("La mejor manera de predecir el futuro es crearlo")
                case 4:
                      print("Adios")
                      Activo = False
            Accion = ""  # Reset Accion to ask for next action
                