# Punky loves wearing different colored socks, but Henry can't stand it.
#
# Given an array of different colored socks, return a pair depending on who was picking them out.
#
# Example:
#
# get_socks('Punky', ['red','blue','blue','green']) -> ['red', 'blue']
# Note that Punky can have any two colored socks, in any order, as long as they are different and both exist. Henry always picks a matching pair.

def get_socks(name, socks):
    if name == 'Punky':
        if len(socks) < 2:
            return []

        first = socks[0]
        for sock in socks[1:]:
            if sock != first:
                return [first, sock]
        return []

    else:
        seen = set()
        for sock in socks:
            if sock in seen:
                return [sock, sock]
            seen.add(sock)
        return []