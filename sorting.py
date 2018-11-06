def bubble_sort(L):

    """
    >>> L = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> bubble_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    end = len(L) - 1

    while end > 0:
        for i in range(end):
            if L[i] > L[i+1]:
                 L[i] , L[i+1] = L[i+1], L[i]
        end -= 1

def get_min_value_index(L, i):
    """ (list, int) -> int

    Return the index of the smallest item in L[i:].

    >>> get_min_value_index([2, 7, 3, 5], 1)
    2
    """
    min_i = i
    
    for j in range(i+1, len(L)):
        if L[min_i] > L[j]:
            min_i = j
    return min_i
        
def selection_sort(L):

    """
    >>> L = [3, 7, 2, 5]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    i = 0 
    while i < len(L)-1:
        min_i = get_min_value_index(L, i)
        L[i] , L[min_i] = L[min_i], L[i]
        i+=1

def insert(L, i):
    """ (list, int) -> NoneType

    Precondition: L[:i] is sorted from smallest to largest.

    Move L[i] to where it belongs in L[:i + 1].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """
    value = L[i]
    j=i
    while j > 0 and L[j-1] > value:
        L[j] = L[j-1]
        j -= 1
        
    L[j] = value

def insertion_sort(L):
    """
    >>> L = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(len(L)):
        insert(L, i)
