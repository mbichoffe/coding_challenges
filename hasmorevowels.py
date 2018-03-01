"""Does word contain more vowels than non-vowels?

If the word is over half vowels, it should return True:

    >>> has_more_vowels("moose")
    True

If it's half vowels (or less), it's false:

    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

Don't consider "y" as a vowel:

    >>> has_more_vowels("yay")
    False

Uppercase vowels are still vowels:

    >>> has_more_vowels("Aal")
    True
"""


def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""
    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowels_count = 0

    for word in words:

        if word in vowels:
            vowels_count += 1
    return len(word)/2 < vowels_count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
