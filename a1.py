def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(25)
    1
    >>> num_buses(49)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(75)
    2
    >>> num_buses(103)
    3
    """
    bus = n // 50
    if n % 50 > 0:
        bus += 1
        
    return bus

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.0, 0.0, 0.0, 0.00, 0, 0, 0.0, 0])
    (0, 0)
    >>> stock_price_summary([0.2, 0, 0.3, 0.05, 0, 0, 0.1, 0.01])
    (0.66, 0)
    >>> stock_price_summary([-0.2, 0, -0.3, -0.05, 0, 0, -0.1, -0.01])
    (0, -0.66)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    sum_gain = 0
    sum_loss = 0
    for each in price_changes:
        if each > 0:
            sum_gain += each
        elif each < 0:
            sum_loss += each
    tup = (sum_gain, sum_loss)
    return tup

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4, 5, 6]
    >>> nums = []
    >>> swap_k(nums, 1)
    >>> nums
    []
    >>> nums = [10]
    >>> swap_k(nums, 0)
    >>> nums
    [10]
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums, 3)
    >>> nums
    [5, 6, 7, 4, 1, 2, 3]
    """
    if len(L) == 0 or len(L) == 1:
        return

    
    L[:k], L[(len(L)-k):] = L[(len(L)-k):], L[:k]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
