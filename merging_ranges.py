#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python Coding Challenges"""
"""
Your company built an in-house calendar tool called HiCal. You want to add
a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. In HiCal,
a meeting is stored as tuples ↴ of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # meeting from 10:00 – 10:30 am
(6, 9)  # meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of meeting time
ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]
"""


def merge_ranges(lst):
    """
    >>> meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    >>> merge_ranges(meeting_times)
    [(0, 1), (3, 8), (9, 12)]
    >>> meeting_times =   [(1, 10), (2, 6), (3, 5), (7, 9)]
    >>> merge_ranges(meeting_times)
    [(1, 10)]
    >>> meeting_times = [(1, 2), (2, 3)]
    >>> merge_ranges(meeting_times)
    [(1, 3)]
    >>> meeting_times =   [(1, 5), (2, 3)]
    >>> merge_ranges(meeting_times)
    [(1, 5)]

    """
    # sort by start time
    sorted_meetings = sorted(lst, key=lambda x: x[0])

    # start merged meetings with the first meeting times
    merged_meetings = [sorted_meetings[0]]

    for sorted_meeting_start, sorted_meeting_end in sorted_meetings[1:]:
        latest_added_meeting_start,\
            latest_added_meeting_end = merged_meetings[-1]

        # if the meeting times overlap, add the latest meeting end time
        if sorted_meeting_start <= latest_added_meeting_end:

            merged_meetings[-1] = (latest_added_meeting_start,
                                   max(latest_added_meeting_end,
                                       sorted_meeting_end))
        else:
            merged_meetings.append((sorted_meeting_start, sorted_meeting_end))

    return merged_meetings



if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print("HURRAY!")
