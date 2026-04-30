# Write a function to calculate the centroid of 3D coordinates.

# Return the results as a list of 3 floats.

def centroid(points: list[list[float]]) -> list[float]:
    if len(points) == 0:
        return [0.0, 0.0, 0.0]
    
    return [sum(coord) / len(points) for coord in zip(*points)]