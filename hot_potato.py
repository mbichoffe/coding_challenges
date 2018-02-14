#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
We will implement a general simulation of Hot Potato. Our program will input a
list of names and a constant, call it “num,” to be used for counting.
It will return the name of the last person remaining after repetitive counting
by num.

To simulate the circle, we will use a queue.
Assume that the child holding the potato will be at the front of the queue.
Upon passing the potato, the simulation will simply dequeue and then
immediately enqueue that child, putting her at the end of the line.
She will then wait until all the others have been at the front before it will
be her turn again. After num dequeue/enqueue operations, the child at the front
will be removed permanently and another cycle will begin. This process will
continue until only one name remains (the size of the queue is 1).

    >>> hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7)
    'Susan'

"""

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    gamequeue = Queue()
    for name in namelist:
        gamequeue.enqueue(name)

    while gamequeue.size() > 1:
        for i in range(num):
            gamequeue.enqueue(gamequeue.dequeue())

        gamequeue.dequeue()

    return gamequeue.dequeue()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
