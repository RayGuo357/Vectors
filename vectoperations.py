import math
from vectors import Vector
from points import Point

# TODO: Unit vector
#       Scalar
#       Addition & Subtraction?

# Function to multiply a vector by the scalar
def scalar(v1, k):
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("'v1' must be an object of Vector or an array")

    if isinstance(v1, list):
        v1 = Vector(v1[0], v1[1], v1[2])

    x, y, z = v1.to_array()

    return Vector(x * k, y * k, z * k)

# Function to make a vector out of 2 points
def difference_points(p1, p2 = Point(0, 0, 0)):
    if not (isinstance(p1, Point) or isinstance(p1, list)):
        raise TypeError("'p1' must be an object of Point or an array")
    if not (isinstance(p2, Point) or isinstance(p2, list)):
        raise TypeError("'p2' must be an object of Point or an array")

    if isinstance(p1, list):
        p1 = Point(p1[0], p1[1], p1[2])

    if isinstance(p2, list):
        p2 = Point(p2[0], p2[1], p2[2])

    x, y, z = p1.to_array()
    a, b, c = p2.to_array()

    return Vector(x - a, y - b, z - c)

# Function to create point from a point and a vector
def sum_point_vector(p1, v1):
    if not (isinstance(p1, Point) or isinstance(p1, list)):
        raise TypeError("'p1' must be an object of Point or an array")
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("v1 must be an object of Vector or an array")

    if isinstance(p1, list):
        p1 = Point(p1[0], p1[1], p1[2])
    if isinstance(v1, list):
        v1 = Vector(v1[0], v1[1], v1[2])

    x, y, z = p1.to_array()
    a, b, c = v1.to_array()

    return Point(x + a, y + b, z + c)

# Function for magnitude of a vector
def magnitude(v1):
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("Must be an object of Vector or an array")

    if isinstance(v1, list):
        v1 = Vector(v1[0], v1[1], v1[2])

    return math.sqrt(sum(k ** 2 for k in v1.to_array()))

# Function for the unit vector/ normilization of a vector
def unit_vector(v1):
    return scalar(v1, 1 / magnitude(v1))

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

    return sum(v1.to_array()[k] * v2.to_array()[k] for k in range(3))

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
