from vectors import Vector

# Function to clean up code and add functionaliy for arrays as well as obj of Vector
def assign_var(v1 = [0, 0, 0], v2 = [0, 0, 0]):
    global x1, y1, z1, x2, y2, z2

    if isinstance(v1, list):
        x1 = v1[0]
        y1 = v1[1]
        z1 = v1[2]
    else:
        x1 = v1.get_x()
        y1 = v1.get_y()
        z1 = v1.get_z()

    if isinstance(v2, list):
        x2 = v2[0]
        y2 = v2[1]
        z2 = v2[2]
    else:
        x2 = v2.get_x()
        y2 = v2.get_y()
        z2 = v2.get_z()



# Function for dot product of 2 vectors
def dot_product(v1, v2) -> int:
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("v1 must be an object of Vector or an array")
    if not (isinstance(v2, Vector) or isinstance(v2, list)):
        raise TypeError("v2 must be an object of Vector or an array")

    assign_var(v1, v2)

    product = 0
    product += x1 * x2
    product += y1 * y2
    product += z1 * z2
    return product

# Function for cross product of 2 vectors
def cross_product(v1, v2) -> Vector:
    if not (isinstance(v1, Vector) or isinstance(v1, list)):
        raise TypeError("v1 must be an object of Vector or an array")
    if not (isinstance(v2, Vector) or isinstance(v2, list)):
        raise TypeError("v2 must be an object of Vector or an array")

    assign_var(v1, v2)

    x = (y1 * z2) - (z1 * y2)
    y = (z1 * x2) - (x1 * z2)
    z = (x1 * y2) - (y1 * x2)
    return Vector(x, y, z)
