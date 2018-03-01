"""
Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and a
dequeue method and it should be "first in first out" (FIFO).

Optimize for the time cost of mm calls on your queue. These can be any mix of
enqueue and dequeue calls.

Assume you already have a stack implementation and it gives O(1)O(1) time push
and pop.
"""

class Staqueue(object):
    def __init__(self):
        self.staqueue1 = [] #empty stack
        self.staqueue2 = []

    def enqueue(self, item):

        self.staqueue1.append(item)

    def dequeue(self, item):

        if len(self.staqueue2):
            return self.staqueue2.pop()
        else:
            for _ in range(len(self.staqueue1)):
                self.staqueue2.append(self.staqueue1.pop())

        if len(self.staqueue2) == 0:
            raise IndexError("Can't dequeue from empty queue")

        return self.staqueue2.pop()


"""
Complexity:
enqueue is O(1) 
dequeue is O(1) if staqueue 2 has items on it.

Notice that the more expensive a dequeue on an empty out_stack is 
(that is, the more items we have to move from in_stack to out_stack),
the more O(1)O(1)-time dequeues off of a non-empty out_stack it wins us in the
future. Once items are moved from in_stack to out_stack they just sit there,
ready to be dequeued in O(1) time. An item never moves "backwards"
in our data structure.

We might guess that this "averages out" so that in a set of mm enqueues and
dequeues the total cost of all dequeues is actually just O(m)O(m).
To check this rigorously, we can use the accounting method, 
counting the time cost per item instead of per enqueue or dequeue.

So let's look at the worst case for a single item, which is the case where it
is enqueued and then later dequeued. In this case, the item enters in_stack
(costing 1 push), then later moves to out_stack (costing 1 pop and 1 push),
then later comes off out_stack to get returned (costing 1 pop).

Each of these 4 pushes and pops is O(1)O(1) time.
So our total cost per item is O(1)O(1). 
Our mm enqueue and dequeue operations put
m or fewer items into the system, giving a total runtime of O(m).
"""

