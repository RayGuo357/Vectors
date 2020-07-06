from vectors import Vector

def dot_product(v1: Vector, v2: Vector) -> int:
    if not isinstance(v1, Vector):
        raise TypeError("v1 must be a vector")
    elif not isinstance(v2, Vector):
        raise TypeError("v2 must be a vector")
    else:
        product = 0
        product += v1.get_x() * v2.get_x()
        product += v1.get_y() * v2.get_y()
        product += v1.get_z() * v2.get_z()
        return product

def cross_product(v1: Vector, v2: Vector) -> Vector:
    if not isinstance(v1, Vector):
        raise TypeError("v1 must be a vector")
    elif not isinstance(v2, Vector):
        raise TypeError("v2 must be a vector")
    else:
        x = (v1.get_y() * v2.get_z()) - (v1.get_z() * v2.get_y())
        y = (v1.get_z() * v2.get_x()) - (v1.get_x() * v2.get_z())
        z = (v1.get_x() * v2.get_y()) - (v1.get_y() * v2.get_x())
        return Vector(x, y, z)
