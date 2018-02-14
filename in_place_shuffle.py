#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have
the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random
integer that is >= floor and <= ceiling.
"""
import random

def naive_in_place_shuffle(arr):
    floor = 0
    ceiling = len(arr)-1

    for i, var in enumerate(arr):
        r = random.randint(floor, ceiling)
        arr[i], arr[r] = arr[r], arr[i]

    return arr

"""
This implementation does not give us a uniform random distribution.

Why? We could calculate the exact probabilities of two outcomes to show
they aren't the same. But the math gets a little messy. Instead,
think of it this way:

Suppose our list had 33 elements: [a,b,c]. This means it'll make 33 calls to
get_random(0, 2). That's 33 random choices, each with 33 possibilities.
So our total number of possible sets of choices is 3*3*3=27
Each of these 2727 sets of choices is equally probable.
But our function has 27 equally-probable sets of choices. 27
is not evenly divisible by 66. So some of our 66 possible outcomes
will be achievable with more sets of choices than others.

We can simply choose a random item to be the first item in the resulting list,
then choose another random item (from the items remaining) to be the second
item in the resulting list, etc.

Assuming these choices were in fact random, this would give us a uniform
shuffle. To prove it rigorously, we can show any given item aa has the same
probability (1/n) of ending up in any given spot.

First, some stats review: to get the probability of an outcome, 
you need to multiply the probabilities of all the steps required for
that outcome.
"""

def in_place_shuffle(arr):


    ceiling = len(arr)-1
    
    for _idx in range(0, len(arr)):

        r = random.randint(_idx, ceiling)

        if r != _idx:
            arr[_idx], arr[r] = arr[r], arr[_idx]

    return arr




