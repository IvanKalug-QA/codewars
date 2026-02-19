# Wikipedia: The Baum–Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:

# bn = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
# bn = 0 otherwise;

# for n ≥ 0.

# Define a generator function baum_sweet that sequentially generates the values of this sequence.

# It will be tested for up to 1 000 000 values.

# Note that the binary representation of 0 used here is not 0 but the empty string ( which does not contain any blocks of consecutive 0s ).

def baum_sweet():
    n = 0
    while True:
        if n == 0:
            yield 1
        else:
            binary = bin(n)[2:]
            valid = True
            zeros_count = 0
            for bit in binary:
                if bit == '0':
                    zeros_count += 1
                else:
                    if zeros_count > 0 and zeros_count % 2 == 1:
                        valid = False
                        break
                    zeros_count = 0
            
            if valid and zeros_count > 0 and zeros_count % 2 == 1:
                valid = False
            yield 1 if valid else 0
        n += 1
