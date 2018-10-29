def collect_vowels(s):
    ''' (str) -> str
    Return vowels (a, e, i, o, and u) from s.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('bghfdh')
    ''
    '''
    vowels = ''

    for c in s:
        if c in 'aeiouAEIOU':
            vowels += c

    return vowels

def count_vowels(s):
    ''' (str) -> int
    Return the number of vowels (a, e, i, o, and u) in s.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('bghfdh')
    ''
    '''
    num_vowels = 0

    for c in s:
        if c in 'aeiouAEIOU':
            num_vowels += 0

    return num_vowels

import doctest
doctest.testmod()

''' doctest lets you test your code by running examples
embedded in the documentation and verifying that they produce
the expected results. It works by parsing the help text to find examples,
running them, then comparing the output text against the expected value
'''
