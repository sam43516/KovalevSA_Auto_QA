import math

def square(side_size):
    side_size = side_size*side_size
    return math.ceil(side_size)

print(square(5))