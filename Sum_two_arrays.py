# Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, and returns the sum of those two arrays.
#
# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata, meaning it would equal 329. The output should be an array of the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). Examples are given below of what two arrays should return.
#
# [3,2,9],[1,2] --> [3,4,1]
# [4,7,3],[1,2,3] --> [5,9,6]
# [1],[5,7,6] --> [5,7,7]
# If both arrays are empty, return an empty array.
#
# In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:
#
# [3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962

def sum_arrays(array1,array2):
    if not len(array1) and not len(array2):
        return []
    elif not len(array1):
        return array2
    elif not len(array2):
        return array1
    res = ''
    res1 = ''
    minus = False
    minus1 = False
    for i in array1:
        if i < 0:
            minus = True
            res += str(i)[1]
        else:
            res += str(i)
    for i in array2:
        if i < 0:
            minus1 = True
            res1 += str(i)[1]
        else:
            res1 += str(i)
    if minus and minus1:
        res = -int(res)
        res1 = -int(res1)
    elif minus:
        res = -int(res)
        res1 = int(res1)
    elif minus1:
        res1 = -int(res1)
        res = int(res)
    else:
        res = int(res)
        res1 = int(res1)
    l = []
    stack = list()
    for i in str(res + res1):
        if i == '-':
            stack.append('-')
        else:
            if len(stack):
                l.append(int(stack.pop() + i))
            else:
                l.append(int(i))
    return l