#Ejercicio Practica 2
#Escribir un programa que pregunte el correo electrónico del usuario en la consola 
#y muestre por pantalla nombre de usuario (o vanity) servidor o dominio (google, hotmail, yandex, etc)
#y extensión (.ar, com, .cl, etc). El dominio lo debe mostrar con mayúsculas (Google, Hotmail, Yahoo)

#loco_quique@gmail.com.ar
#vanity: loco_quique
#Dominio: Gmail
#extensión: .com.ar


email = input("Ingrese su correo electronico: ")

email = email.split("@")

vanity = email[0]
print("Su nombre de usuario es", vanity)

dominio_y_extension = email[1]

dominio = dominio_y_extension[:dominio_y_extension.index(".")]
dominio = dominio.capitalize()
extension = dominio_y_extension[dominio_y_extension.index("."):]

print("El dominio de su correo es", dominio)
print("La extension de su correo es", extension)

