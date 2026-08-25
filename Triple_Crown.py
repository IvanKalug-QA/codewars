# Welcome to the world of the National Football League!

# In the NFL the Triple Crown is given when a receiver has the most receiving yards, the most receiving touchdowns and the most receptions in a single season.

# This year Cooper Kupp managed to get it, however it is quite rare because the last one was in 2005 by Steve Smith.

# Now you will receive a dictionary with the following keys (will always contain each):

# Cooper Kupp

# Justin Jefferson

# Davante Adams

# Each key will have another dictionary as their values with the following keys:

# Receiving yards (value between 1500-2000)

# Receiving touchdowns (value between 10-20)

# Receptions (value between 90-120)

# If one receiver has the most in each category you have to return his name. If there is no receiver with the most values in all categories you should return 'None of them'.

# Example:

# {
#   'Cooper Kupp': 
#     {
#     'Receiving yards': 1786, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 117
#     },
#   'Justin Jefferson': 
#     {
#     'Receiving yards': 1700, 
#     'Receiving touchdowns': 17, 
#     'Receptions': 115
#     },
#   'Davante Adams': 
#     {
#     'Receiving yards': 1650, 
#     'Receiving touchdowns': 16, 
#     'Receptions': 110
#     }
# }

# # The output should be 'Cooper Kupp' since he has more receiving yards, more receiving touchdowns and more receptions as well
# Example with two receivers sharing values in at least one category:

# {
#   'Cooper Kupp': 
#     {
#     'Receiving yards': 1900, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 117
#     },
#   'Justin Jefferson': 
#     {
#     'Receiving yards': 1800, 
#     'Receiving touchdowns': 17, 
#     'Receptions': 116
#     },
#   'Davante Adams': 
#     {
#     'Receiving yards': 1900, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 110
#     }
# }

# # The output should be 'None of them' since they are tied on receiving yards and receiving touchdowns

def triple_crown(receivers):
    max_yards = max(receivers[player]['Receiving yards'] for player in receivers)
    max_tds = max(receivers[player]['Receiving touchdowns'] for player in receivers)
    max_receptions = max(receivers[player]['Receptions'] for player in receivers)
    
    yards_leaders = [player for player in receivers if receivers[player]['Receiving yards'] == max_yards]
    tds_leaders = [player for player in receivers if receivers[player]['Receiving touchdowns'] == max_tds]
    receptions_leaders = [player for player in receivers if receivers[player]['Receptions'] == max_receptions]
    
    if len(yards_leaders) > 1 or len(tds_leaders) > 1 or len(receptions_leaders) > 1:
        return 'None of them'
    
    if yards_leaders[0] == tds_leaders[0] == receptions_leaders[0]:
        return yards_leaders[0]
    
    return 'None of them'