"""
Given a list of integers, find the highest product
you can get from three of the integers.


The input list_of_ints will always have at least three integers.
>>> brute_highest_product([-10, -10, 1, 3, 2])
300
"""

##BRUTE FORCE###

def brute_highest_product(list_of_ints):
    highest_product = 1

    for i in list_of_ints:
        for j in list_of_ints:
            for k in list_of_ints:
                product = i*j*k
                if product > highest_product:
                    highest_product = product
    return highest_product

# O(n3) runtime
# So bad!

# How can we keep track of the highest_product of 3 as we do one walk
# through the list?
# Sorting would give us n log n.
# What should we keep track of to handle all possible scenarios?
# Strategy 1: Keep track of highest_2 and lowest_2 (most negative) numbers
    # if the current number times some combination of those is higher than 
    # the current highest_product_of_3, we have a new highest_product_of_3!
# Strategy 2: keep track of highest product of 2 and lowest product of 2
# Also keep track of the current lowest and current highest


def highest_product(list_of_ints):
    """
    input = list of integers (lenght > 3)
    output = integer (highest product from 3 of the integers)
    >>> highest_product([-10, -10, 1, 3, 2])
    300
    >>> highest_product([1, 10, -5, 1, -100])
    5000
    """
    # we're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    # except this one--we pre-populate it for the first *3* items.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for num in list_of_ints[2:]: # walk throguh items, starting at index 2
        highest_product_of_3 = max(highest_product_of_3,
                                   highest_product_of_2*num,
                                   lowest_product_of_2*num)
        # do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2, 
                                   num*highest,
                                   num*lowest)
        lowest_product_of_2 = min(lowest_product_of_2,
                                  num * highest,
                                  num * lowest)
        # check for new highest
        highest = max(num, highest)
        lowest = max(num, lowest)

    return highest_product_of_3



if __name__ == "__main__":
    import doctest
    doctest.testmod()