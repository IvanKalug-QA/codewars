# Implement a function to calculate the distance between two points in n-dimensional space. The two points will be passed to your function as arrays of the same length.

# Round your answers to two decimal places.

def euclidean_distance(point1, point2):
    sum_of_squares = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    distance = sum_of_squares ** 0.5
    return round(distance, 2)