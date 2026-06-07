# Overview
# A field is about to be divided into 4 equal sections by two perpendicular roads crossing through the center.

# The field is represented by a rectangular grid of integers, where each number represents the land value of a parcel.

# Task
# Given a grid area (list[list[int]]), return the maximum total land value among the four sections.

# Any parcel occupied by the roads is not part of any section.

# For odd dimensions, the middle row/column is occupied by the roads.
# For even dimensions, the roads pass between the two middle rows/columns.
# Notes
# The grid is guaranteed to be rectangular
# Input constraints : 2 <= grid rows, grid columns <= 100
# Values can be negative
# Example
# 1. [[4,6,7,2],          4 6 | 7 2
#     [0,3,7,6],    =>    0 3 | 7 6
#     [7,9,4,2],          ----+-----
#     [1,1,2,0]]          7 9 | 4 2
#                         1 1 | 2 0
                        
#     Output : 22 (7+2+7+6)
    
# 2. [[0,0,3,4,1],        0 0 | 4 1
#     [6,8,9,1,4],        6 8 | 1 4
#     [9,0,3,6,1],   =>   ----+----
#     [8,2,4,6,3],        8 2 | 6 3
#     [1,6,3,7,8]]        1 6 | 7 8
        
#     Output : 24 (6+3+7+8)
    
# 3. [[2,5,1,0,4,5],      2 5 1 | 0 4 5
#     [5,6,8,1,3,0],      5 6 8 | 1 3 0
#     [5,9,1,3,7,4],  =>  ------+------
#     [8,9,1,2,4,5],      8 9 1 | 2 4 5
#     [3,5,7,0,1,2]]      3 5 7 | 0 1 2
    
#     Output : 33 (8+9+1+3+5+7)


def max_land_value(area: list[list[int]]) -> int:
    rows = len(area)
    cols = len(area[0])
    
    if rows % 2 == 1:
        top_end = rows // 2 - 1
        bottom_start = rows // 2 + 1
    else:
        top_end = rows // 2 - 1
        bottom_start = rows // 2
    
    if cols % 2 == 1:
        left_end = cols // 2 - 1
        right_start = cols // 2 + 1
    else:
        left_end = cols // 2 - 1
        right_start = cols // 2
    
    tl_sum = 0
    for i in range(top_end + 1):
        for j in range(left_end + 1):
            tl_sum += area[i][j]
    
    tr_sum = 0
    for i in range(top_end + 1):
        for j in range(right_start, cols):
            tr_sum += area[i][j]
    
    bl_sum = 0
    for i in range(bottom_start, rows):
        for j in range(left_end + 1):
            bl_sum += area[i][j]
    
    br_sum = 0
    for i in range(bottom_start, rows):
        for j in range(right_start, cols):
            br_sum += area[i][j]
    
    return max(tl_sum, tr_sum, bl_sum, br_sum)