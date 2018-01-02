"""
A crack team of love scientists from OkEros (a hot new dating site) have
devised a way to represent dating profiles as rectangles on a two-dimensional
plane.
They need help writing an algorithm to find the intersection of two users'
love rectangles. They suspect finding that intersection is the key to a
matching algorithm so powerful it will cause an immediate acquisition by
Google or Facebook or Obama or something.

Write a function to find the rectangular intersection of two given
love rectangles.

"""


def get_intersection(dict1, dict2):
    """
    Find the rectangular intersection of two given rectangles.

    >>> rectangle1 = {
    ...         'left_x': 1,
    ...         'bottom_y': 1,
    ...         # width and height
    ...         'width': 6,
    ...         'height': 3,
    ...         }
    >>> rectangle2 = {
    ...         # coordinates of bottom-left corner
    ...         'left_x': 5,
    ...         'bottom_y': 2,
    ...         # width and height
    ...         'width': 3,
    ...         'height': 6,
    ...         }
    >>> get_intersection(rectangle1, rectangle2)
    {'left_x': 5, 'bottom_y': 2, 'width': 2, 'height': 2}
    >>> rectangle1 = {
    ...         'left_x': 1,
    ...         'bottom_y': 1,
    ...         # width and height
    ...         'width': 2,
    ...         'height': 2,
    ...         }
    >>> rectangle2 = {
    ...         # coordinates of bottom-left corner
    ...         'left_x': 5,
    ...         'bottom_y': 3,
    ...         # width and height
    ...         'width': 3,
    ...         'height': 6,
    ...         }
    >>> get_intersection(rectangle1, rectangle2)
    {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}

    """
    love_rectangle = {
        'left_x': None,
        'bottom_y': None,
        'width': None,
        'height': None
    }
    love_rectangle['left_x'], love_rectangle['width'] = find_overlap(
        dict1['left_x'], dict1['width'], dict2['left_x'], dict2['width'])

    love_rectangle['bottom_y'], love_rectangle['height'] = find_overlap(
        dict1['bottom_y'], dict1['height'], dict2['bottom_y'], dict2['height'])

    return love_rectangle


def find_overlap(start1, length1, start2, length2):
    """Find overlapping range between rectangle1 and rectangle2.

    >>> find_overlap(5,3,1,6)
    (5, 2)
    >>> find_overlap(5,3,1,2)
    (None, None)
    """
    bottom_right1 = start1 + length1
    bottom_right2 = start2 + length2
    # find lowest ("leftmost") range end:
    highest_bottom_left = max(start1, start2)
    # find highest ("rightmost") range start:
    lowest_bottom_right = min(bottom_right1, bottom_right2)
    # edge case: no intersection
    if lowest_bottom_right <= highest_bottom_left:
        return (None, None)
    overlap_width = lowest_bottom_right - highest_bottom_left

    return (highest_bottom_left, overlap_width)  # return start point, lenght
