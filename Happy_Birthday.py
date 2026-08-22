# It's your best friend's birthday! You already bought a box for the present. Now you want to pack the present in the box. You want to decorate the box with a ribbon and a bow.

# But how much cm of ribbon do you need?

# Write the method wrap that calculates that!

# A box has a height, a width and a length (in cm). The ribbon is crossed on the side with the largest area. Opposite this side (also the side with the largest area) the loop is bound, calculate with 20 cm more tape.

#   wrap(17,32,11) => 162
#   wrap(13,13,13) => 124
#   wrap(1,3,1) => 32
# Notes:
# height, width and length will always be >0

def wrap(height, width, length):
    area_hw = height * width
    area_wl = width * length
    area_hl = height * length
    
    if area_hw >= area_wl and area_hw >= area_hl:
        ribbon = 2 * (height + length) + 2 * (width + length) + 20
    elif area_wl >= area_hw and area_wl >= area_hl:
        ribbon = 2 * (width + height) + 2 * (length + height) + 20
    else:
        ribbon = 2 * (height + width) + 2 * (length + width) + 20
    
    return ribbon