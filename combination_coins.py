"""
Your quirky boss collects rare, old coins...
They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢), your program would output 44—the number of ways to make 44¢ with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
"""
Class Change(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):

    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")

    # base cases
    elif n in [0, 1]:
        return n

    # see if we've already calculated this
    print self.memo
    if n in self.memo:
        print "grabbing memo[%i]" % n
        return self.memo[n]

    print "computing fib(%i)" % n
    result = self.fib(n - 1) + self.fib(n - 2)

    # memoize
    self.memo[n] = result

    return result

    def make_change_bottom_up(amount, coins, index=0):
        #base cases

        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            return self.memo[memo_key]

        if amount == 0:
            return 1

        if index >= len(coins):
            return 0

        num_possibilities = 0

        current_coin = coins[index]

        amount_with_coin = 0

        while amount_with_coin <= amount:
            remaining = amount - amount_with_coin
            num_possibilities += make_change_bottom_up(remaining, coins, index + 1)

            amount_with_coin += current_coin

        self.memo[memo_key] = num_possibilities
        return num_possibilities
    """
    This answer is quite good. It certainly solves our duplicate work problem.
    It takes O(n*m)O(n∗m) time and O(n*m)O(n∗m) space, where n is the size of
    amount and m is the number of items in denominations.
    However, we can do better. Because our method is recursive it will build up 
    a large call stack ↴ of size O(m)O(m). Of course, this cost is eclipsed by the memory cost of memo, which is O(n*m)O(n∗m). But it's still best to avoid building up a large stack like this, because it can cause a stack overflow
    """

    #without recursion
def make_change_for_loop(amount, coins, index=0):
    #base cases
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    num_possibilities = 0
    for i in xrange(index, len(coins)):

        num_possibilities += make_change_for_loop(amount - coins[i], coins, i)

    return num_possibilities


    # bottom up solution:
    """
    Our recursive approach was top-down because it started with the final
    value for amount and recursively broke the problem down into subproblems
    with smaller values for amount. What if instead we tried to compute the
    answer for small values of amount first, and use those answers to
    iteratively compute the answer for higher values until arriving at the
    final amount?

    The number of new ways we can make a higher_amount when we account for
    a new coin is simply ways_of_doing_n_cents[higher_amount - coin],
    where we know that value already includes combinations involving coin
    (because we went bottom-up, we know smaller values have already
    been calculated).

    """

    def change_possibilities_bottom_up(amount, denominations):
        ways_of_doing_n_cents = [0] * (amount + 1)
        ways_of_doing_n_cents[0] = 1 # only one way to do 0 cent

        for coin in denominations:
            for higher_amount in xrange(coin, amount+1):
                higher_amount_remainder = higher_amount - coin
                ways_of_doing_n_cents[higher_amount] += \
                    ways_of_doing_n_cents[higher_amount_remainder]

        return ways_of_doing_n_cents[amount]


"""
O(n∗m) time and O(n)O(n) additional space, where nn is the amount of money 
and mm is the number of potential denominations.
"""
