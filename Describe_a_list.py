# Write function describeList which returns "empty" if the list is empty or "singleton" if it contains only one element or "longer"" if more.

def describe_list(lst):
    return "empty" if not lst else "singleton" if len(lst) == 1 else "longer"