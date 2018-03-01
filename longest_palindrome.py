#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 

Example:

Input: "cbbd"

Output: "bb"

"""
"""
Approach = Expand around center
We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center,
and there are only 2n - 12n−1 such centers.

You might be asking why there are 2n - 1 but not n centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters
(such as ”abba”) and its center are between the
two ’b’s.
"""
def palindrome_count(string, left, right):
    while left >= 0 and r < len(string) and string[left] == string[right]:
        left -= 1
        right +=1
    return string[left+1:right]

def get_longest_palindrome(s):
    longest_palindrome = ""

    for i in range(len(s)):
        #odd length palindrome
        pal_length = palindrome_count(s, i, i)

        longest_palindrome = max(longest_palindrome, pal_length)

        #check for even length palindrome
        pal_length = palindrome_count(s, i, i+1)

        longest_palindrome = max(longest_palindrome, pal_length)

    return longest_palindrome

