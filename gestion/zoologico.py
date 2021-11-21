class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = None

    def cantidadTotalAnimales(self):
        resultado = 0
        for i in self._zonas:
            longitud = len(i.getAnimales())
            resultado += longitud
        return resultado

    def agregarZonas(self, zona):
        if self._zonas == None:
            self._zonas = []
        self._zonas.append(zona)

    def setNombre(self, nombre):
        self._nombre = nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def setZona(self, zona):
        self._zonas = zona

    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return self._zonas

