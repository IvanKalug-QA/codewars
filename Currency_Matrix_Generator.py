# On the Forex Market the currency symbols for exchange between two currencies are put together in regards to their strength and weakness. The order of the currency strength is as follows:

# "EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"

# So for AUD the currency matrix would be as follows EURAUD, GBPAUD, AUDNZD, AUDUSD, AUDCAD, AUDCHF, AUDJPY

# Your goal is to generate this currency matrix for a given currency. You can assume that the passed in currency is a valid one.

def generate_currency_matrix(currency):
    strength_order = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    result = []
    
    given_index = strength_order.index(currency)
    
    for i, other_currency in enumerate(strength_order):
        if other_currency == currency:
            continue
        
        if given_index < i:
            result.append(f"{currency}{other_currency}")
        else:
            result.append(f"{other_currency}{currency}")
    
    return result