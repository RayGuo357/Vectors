class Vector():
    def __init__(self, a: int, b: int, c: int):
        if not isinstance(a, int):
            raise TypeError("'a' must be an integer")
        elif not isinstance(b, int):
            raise TypeError("'b' must be an integer")
        elif not isinstance(c, int):
            raise TypeError("'c' must be an integer")
        else:
            self.__a = a
            self.__b = b
            self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b

    def setC(self, c):
        self.__c = c
