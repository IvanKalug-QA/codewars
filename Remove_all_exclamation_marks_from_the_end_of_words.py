# Task
# Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

# Examples
# "Hi!" --> "Hi"
# "Hi!!!" --> "Hi"
# "!Hi" --> "!Hi"
# "!Hi!" --> "!Hi"
# "Hi! Hi!" --> "Hi Hi"
# "!!!Hi !!hi!!! !hi" --> "!!!Hi !!hi !hi"

def remove(st):
    res = []
    for i in st.split():
        idx = -1
        for j in range(len(i) - 1, -1, -1):
            if i[j].isalpha():
                idx = j
                break
        res.append(i[:idx+1])
    return ' '.join(res)