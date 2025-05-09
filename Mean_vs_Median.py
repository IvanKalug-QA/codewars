# Your goal is to implement the method meanVsMedian which accepts an odd-length array of integers and returns one of the following:
#
# 'mean' - in case mean value is larger than median value
# 'median' - in case median value is larger than mean value
# 'same' - in case both mean and median share the same value
# Reminder: Median
#
# Array will always be valid (odd-length >= 3)

from statistics import median
def mean_vs_median(numbers):
    mean = sum(numbers) // len(numbers)
    med = median(numbers)
    return 'median' if med > mean else 'mean' if mean > med else 'same'