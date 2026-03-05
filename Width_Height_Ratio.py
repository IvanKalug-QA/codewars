# We all use 16:9, 16:10, 4:3 etc. ratios every day. Main task is to determine image ratio by its width and height dimensions.

# Function should take width and height of an image and return a ratio string (ex."16:9"). If any of width or height entry is 0 function should throw an exception (or return Nothing).

def calculate_ratio(w, h):
    if w == 0 or h == 0:
        raise ValueError("Width and height must be non-zero")
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(w, h)
    w_reduced = w // common_divisor
    h_reduced = h // common_divisor
    
    return f"{w_reduced}:{h_reduced}"