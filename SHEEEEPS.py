# HI! You have the array of sheeps:

# ['sheep', 'sheep', 'sheep', 'sheep'...]

# But somebody is "sick":

# ['shpee', 'sheep', 'hspee', 'sheep', 'pehes'...]

# You can help them:

# shpee => sheep

# pehes => sheep

# Because shpee and pehes have 1 s, 1 h, 2 e, 1 p.

# shep !=> sheep

# And:

# sheeep !=> sheep

# return array(list) with "sheep". if you can't help - delete.

# Hard register!!!
# A!==a

# Example:
# ShEep !=> sheep

# EXAMPLE:

# ['sheep', 'Shpee', 'pEhEs', 'PPh', 'heep', 'phees']
# return:

# ['sheep', 'sheep']
# Good luck!!!

def reload_sheeps(arr):
    target = "sheep"
    target_count = {}
    for char in target:
        target_count[char] = target_count.get(char, 0) + 1
    
    result = []
    
    for word in arr:
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
        
        if word_count == target_count:
            result.append("sheep")
    
    return result