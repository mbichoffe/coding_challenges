"""
Apple Stock prices

Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am 
local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns 
the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock 
yesterday.
Example:
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
"""
######################
#BRUTE FORCE SOLUTION:
#####################
def get_max_profit_brute(example_value):

    highest_profit = example_value[1] - example_value[0]

    for t1 in range(1, len(example_value)):
        print "current time:", t1, " current value:", example_value[t1]
        for t2 in range(t1+1, len(example_value)):
            profit = example_value[t2] - example_value[t1]
            print "comparing", example_value[t2], "-", example_value[t1]
            print "profit: ", profit
            if profit > highest_profit:
                highest_profit = profit
    print "highest_profit:", highest_profit
    return highest_profit

example1 = [10, 7, 5, 8, 11, 9]
example2 = [10, 7, 5, 3, 2, 1]
get_max_profit_brute(example1)
get_max_profit_brute(example2)

#################
#GREEDY APPROACH
#################
#let's keep track of max profit, min price and current price
# if the difference between current price and min price is > max profit
# we have a new better profit

def get_max_profit(stock_prices):
    """
    For every price, we check if:

    - we can get a better profit by buying at min_price and selling 
    at the current_price
    - we have a new min_price
    """
    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')
    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    # skip the first (0th) time
    # we can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # if we took this out, we'd try to buy *and* sell at time 0.
    # this would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_price in stock_prices[1:]:
        # check if current profit is > max profit:
        potential_profit = current_price - min_price
        # check if current price is lower than min_price
        min_price = min(min_price, current_price)
        # evaluate potential profit
        max_profit = max(max_profit, potential_profit)
    print max_profit
    return max_profit


get_max_profit(example1)
get_max_profit(example2)


