# The four bases found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

# In genetics, GC-content is the percentage of Guanine (G) and Cytosine (C) bases on a DNA molecule that are either guanine or cytosine.

# Given a DNA sequence (a string) return the GC-content in percent.

# For more information about GC-content you can take a look to wikipedia GC-content.

# For example: the GC-content of the following DNA sequence is 50%: "AAATTTCCCGGG".

# Note: You can take a look to my others bio-info kata here

def gc_content(seq):
    if not seq: 
        return 0.0
    
    seq = seq.upper()
    
    gc_count = seq.count('G') + seq.count('C')
    
    return (gc_count / len(seq)) * 100.0