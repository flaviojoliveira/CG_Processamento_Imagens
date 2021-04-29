import numpy
class Vertice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
class Poligono:
    def __init__(self):
        self.sequenciaVertices = []

def setSequenciaVertices(self, sequencia):
     self.sequenciaVertices = sequencia

def getVertices(self):
    return self.sequenciaVertices

class Malha:
 def __init__(self):
     self.vertices = set()
     self.poligonos = set()

 def getVertices(self):
     return self.vertices

 def getPoligonos(self):
     return self.poligonos

 def addPoligono(self,poligono):
     self.poligono.add(poligono)
     self.vertices.add(poligono.getVertices())
