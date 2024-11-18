from .database import dataBase
from ROOT import evd
import pyqtgraph as pg


class wire(dataBase):

    """docstring for wire"""

    def __init__(self):
        super(wire, self).__init__()
        self._process = None

    def getPlane(self, plane):
        return self._process.getArrayByPlane(plane)


class recoWire(wire):

    def __init__(self, geom):
        super(recoWire, self).__init__()
        self._process = evd.DrawWire()
        self._process.initialize()
        self._process.setInput(self._producerName)
        for plane in range(geom.nViews()):
            self._process.setYDimension(geom.readoutWindowSize(),plane)
            print(geom.readoutPadding())
            if geom.readoutPadding() != 0:
                self._process.setPadding(geom.readoutPadding(), plane)

    def setProducer(self, producer):
        self._producerName = producer
        if self._process is not None:
            self._process.setInput(self._producerName)


class rawDigit(wire):

    def __init__(self, geom):
        super(rawDigit, self).__init__()
        self._process = evd.DrawRawDigit()
        for i in range(len(geom._pedestals)):
            self._process.setPedestal(geom._pedestals[i], i)
        self._process.initialize()
        if "boone" in geom.name():
            self._process.SetCorrectData(False)
        else:
            self._process.SetCorrectData(False)
        for plane in range(geom.nViews()):
            self._process.setYDimension(geom.readoutWindowSize(),plane)
            if geom.readoutPadding() != 0:
                self._process.setPadding(geom.readoutPadding(), plane)


    def setProducer(self, producer):
        self._producerName = producer
        if self._process is not None:
            self._process.setInput(self._producerName)
            
    def toggleNoiseFilter(self, filterNoise):
        self._process.SetCorrectData(filterNoise) 
