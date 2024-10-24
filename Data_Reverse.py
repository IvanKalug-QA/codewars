# A stream of data is received and needs to be reversed.
#
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
#
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:
#
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.
#
# The data is given in an array as such:
#
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.

def data_reverse(data):
    bit_counter = 0
    result_array = []
    current_bit_array = []
    for i in data:
        if bit_counter == 8:
            result_array.append(current_bit_array)
            current_bit_array = [i]
            bit_counter = 1
        else:
            bit_counter += 1
            current_bit_array.append(i)
    result_array.append(current_bit_array)
    final_bit_array = []
    while result_array:
        bit_array = result_array.pop()
        for i in bit_array:
            final_bit_array.append(i)
    return final_bit_array