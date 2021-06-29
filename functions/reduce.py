import math

def area(r):
    return math.pi * (r ** 2)

radii = [1,2,3,4]
areas = []

for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

areas = []
print(list(map(area, radii)))