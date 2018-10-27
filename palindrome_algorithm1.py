def is_palindrome(s):
    """ (str() -> bool
    Return True if and only if s is a palindrome
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """

    return reverse(s) == s

def reverse(s):
    """
    Return a reversed version of s.
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    # For each character in s, add that char to the beginning of reverse
    rev = ''
    for ch in s:
        rev = ch + rev
    return rev
