#Country class- creates the country object
class Country:
    #function to create the country object
    def __init__(self, name="", population="", area="", continent=""):
        self._name= name
        self._population= population
        self._area= area
        self._continent= continent

    #function to return the country object
    def __repr__(self):
        return ("%s (pop: %s, size: %s) in %s" % (self._name, self._population, self._area, self._continent))
    #function to retrieve the country name
    def getName (self):
        return self._name
    #function to retrieve the population
    def getPopulation (self):
        return self._population
    #function to retrieve the area
    def getArea (self):
        return self._area
    #function to retrieve the continent
    def getContinent (self):
        return self._continent
    #function to set the population
    def setPopulation (self, population):
        self._population= population
    #function to set the area
    def setArea (self, area):
        self._area= area
    #function to set the continent
    def setContinent (self, continent):
        self._continent= continent


