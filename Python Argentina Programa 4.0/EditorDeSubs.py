archivo = open("entrada.txt", "r")
texto = archivo.readlines()
archivo.close()

simbolos = ["?", ">", "!", ",", "."]
mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
              "T", "U", "V", "W", "X", "Y", "Z"]
digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
archivo = open("salida.txt", "a")
i = 0
for linea in texto:
    if(i > 0 and i < len(texto)):
        if(texto[i][0] in digitos and texto[i-1][-1] == ("\n") and (texto[i-1][-2] in simbolos or texto[i-1][-2] in mayusculas)):
            archivo.write("\n")
    archivo.write(linea)
    i += 1