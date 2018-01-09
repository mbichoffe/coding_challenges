
"""
Theme: Inserts and Getters; ahead-of-time vs just-in-time
You decide to test if your oddly-mathematical heating company 
is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean of all temps we've seen so far
get_mode()—returns a mode of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter methods get_max(), 
get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return
integers. Temperatures will all be inserted as integers. We'll record our 
temperatures in Fahrenheit, so we can assume they'll all be in the range 
0..110.

If there is more than one mode, return any of the modes.

"""
class TempTracker(object):

    def __init__(self):

        #only round number temperatures occur, in range from 0 to 110

        # mode
        self.temperature_ocurrences = [0] * 111
        self.highest_ocurrence = float('-inf')
        self.mode = None
        # max and min
        self.max_temperature = float('-inf')  # negative infinite number - I tried to use None, but you can't compare numbers to None on the max() method
        self.min_temperature = float('inf')  # positive infinite number
        # mean
        self.mean = None
        self.number_of_temperatures = 0
        self.sum_of_all_temperatures = 0.0

    def insert(self, new_temperature):

        self.max_temperature = max(new_temperature, self.max_temperature)
        self.min_temperature = min(new_temperature, self.min_temperature)
        # mean
        self.number_of_temperatures += 1
        self.sum_of_all_temperatures += new_temperature
        self.mean = self.sum_of_all_temperatures / self.number_of_temperatures
        # mode
        self.temperature_ocurrences[new_temperature] += 1
        if self.temperature_ocurrences[new_temperature] > self.highest_ocurrence:
            self.highest_ocurrence = self.temperature_ocurrences[new_temperature]
            self.mode = new_temperature

    def get_max(self):
        return self.max_temperature

    def get_min(self):
        return self.min_temperature

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


"""
What We Learned
This question brings up a common design decision: 
whether to do work just-in-time or ahead-of-time.

Our first thought for this question might have been to use a 
just-in-time approach: have our insert() method simply put the temperature 
in a list, and then have our getters compute e.g. the mode just-in-time, 
at the moment the getter is called.

Instead, we used an ahead-of-time approach: have our insert method 
compute and store our mean, mode, max, and min ahead of time (that is, 
before they're asked for). So our getter just returns the pre-computed 
value in O(1)O(1) time.

In this case, the ahead-of-time approach doesn't just speed up our getters...
it also reduces our space cost. If we tried to compute each metric just-in-time, 
we'd need to store all of the temperatures as they come in, 
taking O(n)O(n) space for nn insert()s.

As an added bonus, the ahead-of-time approach didn't increase our asymptotic 
time cost for inserts, even though we added more work. With some cleverness 
(channeling some greedy ↴ thinking to figure out what we needed to store in 
order to update the answer in O(1)O(1) time), we were able to keep it at 
O(1)O(1) time.

It doesn't always happen this way. Sometimes there are trade-offs between 
just-in-time and ahead-of-time. Sometimes to save time in our getters, 
we have to spend more time in our insert.

In those cases, whether we should prefer a just-in-time approach or an 
ahead-of-time approach is a nuanced question. Ultimately it comes down 
to your usage patterns. Do you expect to get more inserts than gets? 
Do slow inserts have a stronger negative effect on users than slow gets?

We have some more questions dealing with this stuff coming up later.

Whenever you're designing a data structure with inserts and getters, 
think about the advantages and disadvantages of a just-in-time approach
vs an ahead-of-time approach.

"""
