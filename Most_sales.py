# You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:
#
# products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
# amounts: [3, 24, 8]
# prices: [199, 299, 399]
# Return the three product names with the highest revenues (amount * price), in descending order (highest to lowest revenue).
#
# Note: if multiple products have the same revenue, order them according to their original positions in the input list.

def top3(products, amounts, prices):
    result = []
    for i in range(len(products)):
        result.append((amounts[i] * prices[i], products[i], i))
    result.sort(key=lambda x: (x[0], -x[2]), reverse=True)
    return [i[1] for i in result[:3]]