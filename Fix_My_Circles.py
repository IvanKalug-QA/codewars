# Story
# You are a geometricist, a humble member of an ancient, secret order dedicated to creating geometric shapes for use in people's daily lives around the world. One day, you arrive at work to find that a wild Ouroboros has eaten into your circle supply, corrupting many of them! Without these circles, trigonometric functions will cease to exist. People will be unable to study AC power systems. And worst of all, the world will no longer be able to produce LOLLIPOPS! 🍭

# You must fix the corrupted circles as soon as possible - before the world turns square!

# Task
# Write a function circle_mender that takes as an input a string representing a circle with some holes and returns a string with the holes filled.

# The input has the following characteristics:

# It is a string representing an ASCII-art circle;
# It consists of exactly 20 lines, each with 40 characters followed by a newline character;
# The circle is drawn using the pound sign (#), and any holes within it are represented by spaces ( );
# The edges of the circle are never missing.
# Below are some examples to better represent what it is that is expected:

# Example 1:
# -------
# Input:
                                        
                                        
                                        
#                          #####          
#                    #################    
#                  #####           #####  
#                 ####               #### 
#                ######            #######
#                 #######     ########### 
#                  #####################  
#                    #################    
#                          #####          
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
# -------
# Output:
                                        
                                        
                                        
#                          #####          
#                    #################    
#                  #####################  
#                 ####################### 
#                #########################
#                 ####################### 
#                  #####################  
#                    #################    
#                          #####          
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
# Example 2:
# -------
# Input:
                                        
                                        
#           #####                         
#     #################                   
#   #######     #########                 
#  ######         ########                
# #######           #######               
#  ####               ####                
#   #####           #####                 
#     #################                   
#           #####                         
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
# -------
# Output:
                                        
                                        
#           #####                         
#     #################                   
#   #####################                 
#  #######################                
# #########################               
#  #######################                
#   #####################                 
#     #################                   
#           #####                         
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
# Example 3:
# -------
# Input:
                                        
                                        
                                        
                                        
                                        
                                        
                                        
#                  #####                  
#          #####################          
#       ###########################       
#     ########     ##################     
#   ########         ##################   
#   ##########     ####     ###########   
#  ##############             ##########  
#   ###########             ###########   
#   #############             #########   
#     #################     #########     
#       ###########################       
#          #####################          
#                  #####                  
# -------
# Output:
                                        
                                        
                                        
                                        
                                        
                                        
                                        
#                  #####                  
#          #####################          
#       ###########################       
#     ###############################     
#   ###################################   
#   ###################################   
#  #####################################  
#   ###################################   
#   ###################################   
#     ###############################     
#       ###########################       
#          #####################          
#                  #####                

def circle_mender(content: str) -> str:
    lines = content.split('\n')
    
    if len(lines) > 20:
        lines = lines[:20]
    elif len(lines) < 20:
        while len(lines) < 20:
            lines.append('')
    
    result_lines = []
    for line in lines:
        if len(line) > 40:
            line = line[:40]
        line = line.ljust(40)[:40]
        
        first_hash = line.find('#')
        last_hash = line.rfind('#')
        
        if first_hash == -1:
            result_lines.append(line)
            continue
        
        line_chars = list(line)
        for i in range(first_hash, last_hash + 1):
            if line_chars[i] == ' ':
                line_chars[i] = '#'
        
        result_lines.append(''.join(line_chars))
    
    return '\n'.join(result_lines) + '\n'