def limpiar_pantalla():
    if os.name == 'nt':  # En caso de que el programa sea utilizado en Windows
        os.system('cls')
    else:  # En caso de que el programa sea utilizado en UNIX (Linux y macOS)
        os.system('clear')