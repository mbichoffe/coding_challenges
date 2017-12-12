"""
You have a list of integers, and for each index you want to find the product 
of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list 
of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

[84, 12, 28, 21]

by calculating:

[7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.
"""
def get_products_of_all_ints_except_at_index_brute(list_of_ints):
    """Brute force: two loops to multiply the integer at every index
        by the integer at every nested index, unless index == nested_index.
    >>> get_products_of_all_ints_except_at_index_brute([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index_brute([1, 2, 6, 5, 9])
    [540, 270, 90, 108, 60]

    """
    list_of_products = []

    for index, num in enumerate(list_of_ints):
        product = 1
        for nested_index, nested_num in enumerate(list_of_ints):
            if nested_index != index:
                product = product * nested_num
        list_of_products.append(product)
    return list_of_products


#################
#GREEDY APPROACH
#################
# Break down problem into subproblems
"""
The product of all the integers except the integer at each index can be broken 
down into:

1. the product of all the integers before each index
2. the product of all the integers after each index.

"""
def get_products_of_all_ints_except_at_index(int_list):
    """
    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9])
    [540, 270, 90, 108, 60]

    >>> get_products_of_all_ints_except_at_index([1])
    Traceback (most recent call last):
        raise IndexError('Getting the product of numbers at other '
    IndexError: Getting the product of numbers at other indices requires at least 2 numbers


    """
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
    #let's create a list with the length of the original list,
    #and replace None with the value of the prduct so far before each index:
    products_of_all_ints_except_at_index = [None] * len(int_list)
    #[None, None, None...]
    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1

    for i in xrange(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers

    product_before = 1

    for i in xrange(len(int_list)-1, -1, -1):
        products_of_all_ints_except_at_index[i] = product_before * products_of_all_ints_except_at_index[i]
        product_before *= int_list[i]


    return products_of_all_ints_except_at_index
