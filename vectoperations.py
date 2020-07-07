import math
from vectors import Vector

# Function for magnitude of a vector
def magnitude(v1):
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("Must be an object of Vector or an array")

    if isinstance(v1, list):
        v1 = Vector(v1[0], v1[1], v1[2])

    return math.sqrt((v1.get_x() ** 2) + (v1.get_y() ** 2) + (v1.get_z() ** 2))

# Function for dot product of 2 vectors
def dot_product(v1, v2) -> int:
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("v1 must be an object of Vector or an array")
    if not (isinstance(v2, Vector) or isinstance(v2, list)):
        raise TypeError("v2 must be an object of Vector or an array")

    if isinstance(v1, list):
        v1  = Vector(v1[0], v1[1], v1[2])

    if isinstance(v2, list):
        v2 = Vector(v2[0], v2[1], v2[2])

    product = 0
    product += v1.get_x() * v2.get_x()
    product += v1.get_y() * v2.get_y()
    product += v1.get_z() * v2.get_z()
    return product

# Function for cross product of 2 vectors
def cross_product(v1, v2) -> Vector:
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("v1 must be an object of Vector or an array")
    if not (isinstance(v2, Vector) or isinstance(v2, list)):
        raise TypeError("v2 must be an object of Vector or an array")

    if isinstance(v1, list):
        v1  = Vector(v1[0], v1[1], v1[2])

    if isinstance(v2, list):
        v2 = Vector(v2[0], v2[1], v2[2])

    x = (v1.get_y() * v2.get_z()) - (v1.get_z() * v2.get_y())
    y = (v1.get_z() * v2.get_x()) - (v1.get_x() * v2.get_z())
    z = (v1.get_x() * v2.get_y()) - (v1.get_y() * v2.get_x())
    return Vector(x, y, z)
