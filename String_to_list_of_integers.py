# Given a string containing a list of integers separated by commas, write the function that takes said string and returns a new array / list containing all integers present in the string, preserving the order.
#
# Please note that there can be one or more consecutive commas whithout numbers, like so:
#
# "-1,-2,,,,,,3,4,5,,6"
# For example
#
# "-1,-2,3,-4,-5"   --> [-1,-2,3,-4,-5]
# "1,2,3,,,4,,5,,," --> [1,2,3,4,5]
# ",,,,,,,"         --> []

def string_to_int_list(s):
    result = []
    d = ""
    for i in s:
        if i != ",":
            d += i
        else:
            if d != "":
                result.append(int(d))
            d = ""
    if d != "":
        result.append(int(d))
    return result