class Vector():
    def __init__(self, x: int, y: int, z: int):
        if not isinstance(x, int):
            raise TypeError("'x' must be an integer")
        elif not isinstance(y, int):
            raise TypeError("'y' must be an integer")
        elif not isinstance(z, int):
            raise TypeError("'z' must be an integer")
        else:
            self.__x = x
            self.__y = y
            self.__z = z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setZ(self, z):
        self.__z = z
