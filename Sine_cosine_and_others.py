# Given value of sine,implement function which will return sine,cosine,tangent,and cotangent in list. order must be same as in the description and every number must be rounded to 2 decimal places.If tangent or cotangent can not be calculated just don't contain them in result list.

# Trygonometry - https://en.wikipedia.org/wiki/Trigonometry

import math

def sctc(sin):
    cos = math.sqrt(1 - sin**2)
    result = [round(sin, 2), round(cos, 2)]
    if cos != 0:
        tan = sin / cos
        result.append(round(tan, 2))
        
        if sin != 0:
            cot = cos / sin
            result.append(round(cot, 2))
    else:
        if sin != 0:
            cot = cos / sin
            result.append(round(cot, 2))
    
    return result