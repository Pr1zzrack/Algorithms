import math

def distance_between_points(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

point_a = (1, 2)
point_b = (4, 6)
distance = distance_between_points(point_a, point_b)
print("Расстояние между точками:", distance)