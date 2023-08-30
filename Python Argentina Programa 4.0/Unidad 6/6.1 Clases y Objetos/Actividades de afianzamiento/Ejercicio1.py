# Ejercicio 1
# Defina y explique los siguientes conceptos:
# 1. Tipo de Dato Abstracto
# 2. Encapsulación
# 3. Clase
# 4. Variable de Instancia
# 5. Método de Instancia
# 6. Clase Base
# 7. Subclase
# 8. Herencia
# 9. Árbol de Herencia
# 10. Duck Typing


# Tipo de Dato Abstracto:
# Este tipo de dato define un conjunto de atributos y operaciones para un objeto. La unica forma de acceder
# o cambiar los datos de estos atributos es mediante esas operaciones definidas. Programar definiendo
# tipos de datos abstractos permite organizar y definir de mejor manera que es lo que puede hacer cada
# objeto en un programa. Ademas de que permite simplificar el proceso de pasar un programa escrito
# en el Paradigma Imperativo a la Programacion Orientada a Objetos.

# Encapsulación:
# Encapsular un modulo implica que desde otros modulos solamente se pueda acceder a los datos del modulo
# encapsulado mediante sus operaciones. De esta manera podemos utilizar al modulo sin tener que saber como
# esta implementado.

# Clase:
# Podemos implementar los Tipo de Datos Abstractos (TDA) antes mencionados con clases, las cuales pueden encapsular
# los datos y las operaciones que se puede aplicar sobre esos TDAs.

# Variable de Instancia:
# Los atributos que normalmente definimos en modulos, son llamados variables de instancia en un objeto creado por
# el constructor de una clase.

# Método de Instancia:
# Las clases puede definir operaciones las cuales son utilizadas al ser instanciadas por otro objeto que necesite
# a esta clase. Estas operaciones son metodos de instancia.

# Clase Base:
# La Programacion Orientada a Objetos permite el concepto de herencia, que permite que una clase herede el constructor,
# los atributos y las operaciones de otra clase. La clase que provee estos datos se la denomina como clase base.

# Subclase:
# Una subclase es una clase que hereda las caracteristicas de otra clase. Esta subclase puede agregar o redefinir
# operaciones en sus metodos o constructor.

# Herencia:
# La herencia es utilizada para definir la relacion 'es un' entre una clase y otra, es decir, objetos que son
# muy similares pero con algunas variantes como datos u operaciones extra. Podemos describir tambien la relacion
# 'tiene un' o agregacion que apunta a cuando una clase tiene atributos del de tipo de otras clases. En Python todas las clases
# heredan de la clase 'Object' y ademas utilizan agregacion ya que utilizan tipos de datos primitivos.

# Árbol de Herencia:
# Al utilizar herencia podemos definir un arbol que describa que clases heredan de otras clases. En cualquier arbol de herencia
# vamos a tener en la punta de arriba a la clase 'Object' ya que todas las clases heredan de ella.

# Duck Typing:
# Si se desea utilizar un metodo de cierto objeto, no importa que tipo tenga este metodo, lo unico necesario es que el objeto
# tenga el metodo necesitado. Esto es valido en Python y se lo denomina como duck typing