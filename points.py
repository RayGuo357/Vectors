class Point():
    def __init__(self, x: int, y: int, z:int):
        if not (isinstance(x, int) or isinstance(x, float)):
            raise TypeError("'x' must be an integer or float")
        elif not (isinstance(y, int) or isinstance(y, float)):
            raise TypeError("'y' must be an integer or float")
        elif not (isinstance(z, int) or isinstance(z, float)):
            raise TypeError("'z' must be an integer or float")
        else:
            self.__x = x
            self.__y = y
            self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_z(self, z):
        self.__z = z

    def print_point(self):
        print("(%s, %s, %s)" % tuple(self.to_array()))

    def to_array(self):
        return [self.get_x(), self.get_y(), self.get_z()]
