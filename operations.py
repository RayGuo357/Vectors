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

def crossProduct(v1: Vector, v2: Vector) -> int:
    return
