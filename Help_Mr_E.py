# Mr. E Ven only likes even length words. Please create a translator so that he doesn't have to hear those pesky odd length words. For some reason he also hates punctuation, he likes his sentences to flow.
#
# Your translator should take in a string and output it with all odd length words having an extra letter (the last letter in the word). It should also remove all punctuation (.,?!) as well as any underscores (_).
#
# "How did we end up here? We go?" translated becomes-> "Howw didd we endd up here We go"

def evenator(s):
    if not s:
        return ""
    result = []
    for i in s.split():
        r = []
        for j in i:
            if j not in ".,?!_":
                r.append(j)
        if r:
            if len(r) % 2 != 0:
                r.append(r[-1])
        result.append(''.join(r))
    return ' '.join(result).strip()