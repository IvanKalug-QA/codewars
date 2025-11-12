# You're looking through different hex codes, and having trouble telling the difference between #000001 and #100000

# We need a way to tell which is red, and which is blue!

# That's where you create hex color !!!

# It should read an RGB input, and return whichever value (red, blue, or green) is of greatest concentration!

# But, if multiple colors are of equal concentration, you should return their mix!

# red + blue = magenta

# green + red = yellow

# blue + green = cyan

# red + blue + green = white
# One last thing, if the string given is empty, or has all 0's, return black!

# Examples:

# codes = "087 255 054" -> "green"
# codes = "181 181 170" -> "yellow"
# codes = "000 000 000" -> "black"
# codes = "001 001 001" -> "white"

def hex_color(codes):
    if not codes:
        return "black"
    
    rgb = codes.split()
    
    if len(rgb) < 3 or all(x == "000" for x in rgb):
        return "black"
    
    r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
    
    max_val = max(r, g, b)
    
    if r == g == b and r > 0:
        return "white"
    
    max_colors = []
    if r == max_val:
        max_colors.append("red")
    if g == max_val:
        max_colors.append("green")
    if b == max_val:
        max_colors.append("blue")
    
    if len(max_colors) == 1:
        return max_colors[0]
    elif len(max_colors) == 2:
        if "red" in max_colors and "blue" in max_colors:
            return "magenta"
        elif "red" in max_colors and "green" in max_colors:
            return "yellow"
        elif "blue" in max_colors and "green" in max_colors:
            return "cyan"
    else:
        return "white"