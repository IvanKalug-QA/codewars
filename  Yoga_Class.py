# Description
# Lets imagine a yoga classroom as a Square 2D Array of Integers classroom, with each integer representing a person, and the value representing their skill level.

# classroom = [
#             [3,2,1,3],
#             [1,3,2,1],
#             [1,1,1,2],
#             ]
            
# poses = [1,7,5,9,10,21,4,3]
# During a yoga class the instructor gives a list of integers poses representing a yoga pose that each person in the class will attempt to complete.

# A person can complete a yoga pose if the sum of their row and their skill level is greater than or equal to the value of the pose.

# Task
# Your task is to return the total amount poses completed for the entire classroom.

# Example
# classroom = [
#             [1,1,0,1], #sum = 3
#             [2,0,6,0], #sum = 8
#             [0,2,2,0], #sum = 4
#             ]
                    
# poses = [4, 0, 20, 10]

# 3 people in row 1 can complete the first pose
# Everybody in row 1 can complete the second pose
# Nobody in row 1 can complete the third pose
# Nobody in row 1 can complete the fourth pose

# The total poses completed for row 1 is 7

# You'll need to return the total for all rows and all poses.
# Translations are welcomed!

def yoga(classroom, poses):
    total_poses_completed = 0
    row_sums = []
    for row in classroom:
        row_sums.append(sum(row))
    for i in range(len(classroom)):
        row_sum = row_sums[i]
        for person_skill in classroom[i]:
            for pose in poses:
                if row_sum + person_skill >= pose:
                    total_poses_completed += 1
    return total_poses_completed