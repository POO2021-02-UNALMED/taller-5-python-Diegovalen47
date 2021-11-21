


class Animal:

    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def movimiento(self):
        return "despazarse"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return "Mamiferos : " + str(Mamifero.caballos + Mamifero.leones) +\
               "\nAves : " + str(len(Ave.getListado())) + \
               "\nReptiles : " + str(len(Reptil.getListado())) + \
               "\nPeces : " + str(len(Pez.getListado())) + \
               "\nAnfibios : " + str(len(Anfibio.getListado()))

    def toString(self):
        if self._zona != None :
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + \
                   ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + \
                   ", la zona en la que me ubico es " +self.getZona().getNombre() + \
                   ", en el " + self.getZona().getZoo().getNombre()
        else:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + \
                   ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre\

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

