# Ejercicio 13
# Crea una jerarquía de clases que permita organizar los si-
# guientes conceptos: Los animales se dividen en varios subgrupos, al-
# gunos de los cuales son vertebrados: (aves, mamíferos, anfibios, repti-
# les, peces) e invertebrados: artrópodos (insectos, arácnidos, miriápodos,
# crustáceos), anélidos (lombrices, sanguijuelas), moluscos (bivalvos, gas-
# terópodos, cefalópodos), poríferos (esponjas), cnidarios (medusas, pó-
# lipos, corales), equinodermos (estrellas de mar), nematodos (gusanos
# cilíndricos), platelmintos (gusanos planos)


# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
class Animal:
    def __init__(self):
        pass
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
class Vertebrado(Animal):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
# ---------------------------------------------------
class Ave(Vertebrado):
    def __init__(self):
        super().__init__()

class Mamifero(Vertebrado):
    def __init__(self):
        super().__init__()

class Anfibio(Vertebrado):
    def __init__(self):
        super().__init__()

class Reptil(Vertebrado):
    def __init__(self):
        super().__init__()

class Pez(Vertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
# ---------------------------------------------------
class Invertebrado(Animal):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
# ---------------------------------------------------
class Artropodo(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Insecto(Artropodo):
    def __init__(self):
        super().__init__()

class Aracnido(Artropodo):
    def __init__(self):
        super().__init__()

class Miriapodo(Artropodo):
    def __init__(self):
        super().__init__()

class Crustaceo(Artropodo):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Anelido(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Lombriz(Anelido):
    def __init__(self):
        super().__init__()

class Sanguijuela(Anelido):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Molusco(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Bivalvo(Molusco):
    def __init__(self):
        super().__init__()

class Gasteropodo(Molusco):
    def __init__(self):
        super().__init__()

class Cefalopodo(Molusco):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Porifero(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Esponja(Porifero):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Cnidaria(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Medusa(Cnidaria):
    def __init__(self):
        super().__init__()

class Polipo(Cnidaria):
    def __init__(self):
        super().__init__()

class Coral(Cnidaria):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Equinodermo(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class EstrellaDeMar(Equinodermo):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Nematodo(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class GusanoCilindrico(Nematodo):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class Platelminto(Invertebrado):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------
class GusanoPlano(Platelminto):
    def __init__(self):
        super().__init__()
# ---------------------------------------------------