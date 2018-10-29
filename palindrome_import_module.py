import palindrome_algorithm1

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
    n=len(s)
    return palindrome_algorithm1.reverse(s[n - n//2:]) == s[:n//2]
