# A tire size is written in the format "205/55R16" where:

# 205 → tire width in millimeters
# 55 → aspect ratio (sidewall height as a percentage of width)
# 16 → rim diameter in inches
# The construction code between aspect ratio and rim diameter can be R, ZR, B, or D.tire-dimensions-by-code-gs-night-landscape-750.webpGiven a tire size string and a distance in kilometers, return the number of rotations the tire makes.

# Function signature:

# def tire_rotations(tire_size: str, distance_km: float) -> float:
# Examples:

# tire_rotations("205/55R16", 110) ≈ 55410.8047
# tire_rotations("185/65ZR15", 900) ≈ 460947.5423
# tire_rotations("225/45B17", 0) == 0.0
# Notes:

# Use π = math.pi
# 1 inch = 25.4 mm

from math import pi

def tire_rotations(tire_size: str, distance_km: float) -> float:
    if distance_km == 0:
        return 0.0
    
    width_str, rest = tire_size.split('/')
    width_mm = int(width_str)
    
    i = 0
    while i < len(rest) and rest[i].isdigit():
        i += 1
    
    aspect_ratio = int(rest[:i])
    construction_code = rest[i:-2]
    rim_diameter_inches = int(rest[-2:])
    
    sidewall_height_mm = (aspect_ratio / 100) * width_mm
    
    rim_diameter_mm = rim_diameter_inches * 25.4
    total_diameter_mm = rim_diameter_mm + 2 * sidewall_height_mm
    
    circumference_mm = pi * total_diameter_mm
    
    distance_mm = distance_km * 1000 * 1000
    
    rotations = distance_mm / circumference_mm
    
    return rotations