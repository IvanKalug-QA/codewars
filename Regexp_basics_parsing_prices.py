# Implement String#to_cents, which should parse prices expressed as $1.23 and return number of cents, or in case of bad format return nil.
#
# In this kata, for a price to be considered valid, it must start with a dollar sign ($), followed immediately by a decimal number with exactly 2 decimal digits.

def to_cents(amount):
    if not amount.startswith('$') or not amount or '.' not in amount or len(amount.split('.')[-1]) > 2 or amount.count('.') > 1 or amount.count('$') > 1:
        return None
    amount = amount.split('.')
    for i in [amount[0][1:], amount[-1]]:
        for j in i:
            if not i.isdigit():
                return None
    return int(amount[0][1::] + amount[-1])