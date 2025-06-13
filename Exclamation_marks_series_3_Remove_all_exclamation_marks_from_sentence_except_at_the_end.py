# Description:
# Remove all exclamation marks from sentence except at the end.
#
# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!!!"
# "!Hi"     ---> "Hi"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi"

def remove(s):
    result = []
    end = len(s)
    symb = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "!":
            break
        end = i
        symb += 1
    for i in s[:end]:
        if i != "!":
            result.append(i)
    return ''.join(result) + ("!" * symb)