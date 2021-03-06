from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamans, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamans
        self._largoCola = largoCola

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls._listado.append(iguana)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls._listado.append(serpiente)
        cls.serpientes += 1
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
