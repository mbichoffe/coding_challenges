#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pythonds.basic.queue import Queue
import random
"""
Implementation of a printer queue simulation from
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
"""
"""
The printer class will need to track wether is has a current task
If it has, then it's busy and the amount of time needed to complete the task 
can be computed from the number of pages in the task
It also needs to keep track of page rate (draft or quality)
The tick method decrements the internal timer and sets the printer to idle if
the task is completed
"""

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining-1
            if self.timeRemaining <=0:
                self.timeRemaining = 0
                self.currentTask = None

    def busy(self):
        if self.currentTask:
            return True
        return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
# set total time for the simulation (1 hour = 3600s)
# and pages per minute for the printer
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask(): # boolean helper function, decides if a task has been created
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    average_wait = sum(waitingtimes)//len(waitingtimes)

    print("Average Wait {:6.2f} secs and {:3d} tasks remaining".format(average_wait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    # chance that at any given second a task will be created is 1 in 180
    # 10 students printing twice per hour
    if num == 180:
        return True
    return False
for i in range(10):
    simulation(3600, 5)

