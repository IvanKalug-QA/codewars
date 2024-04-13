# Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.
#
# The method should return an array of sentences declaring the state or country and its capital.
#
# Examples
# [{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
# [{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
# [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The cap

def capital(capitals):
    l = list()
    for i in capitals:
        state = i.get("state", False)
        if not state:
            state = i.get("country", False)
        capital = i["capital"]
        l.append(f"The capital of {state} is {capital}")
    return l