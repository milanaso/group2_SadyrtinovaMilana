import math


def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


radius = float(input())

print(sphere_volume(radius))
