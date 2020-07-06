from vectors import Vector

def dotProduct(v1: Vector, v2: Vector) -> int:
    if not isinstance(v1, Vector):
        raise TypeError("v1 must be a vector")
    elif not isinstance(v2, Vector):
        raise TypeError("v2 must be a vector")
    else:
        product = 0
        product += v1.getA() * v2.getA()
        product += v1.getB() * v2.getB()
        product += v1.getC() * v2.getC()
        return product

def crossProduct(v1: Vector, v2: Vector) -> Vector:
    if not isinstance(v1, Vector):
        raise TypeError("v1 must be a vector")
    elif not isinstance(v2, Vector):
        raise TypeError("v2 must be a vector")
    else:
        x = (v1.getY() * v2.getZ()) - (v1.getZ() * v2.getY())
        y = (v1.getZ() * v2.getX()) - (v1.getX() * v2.getZ())
        z = (v1.getX() * v2.getY()) - (v1.getY() * v2.getX())
        return Vector(x, y, z)
