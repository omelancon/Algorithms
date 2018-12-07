def flatten(l):
    output = []
    while l:
        output.append(l[1])
        l = l[0]

    return output[::-1]


def binary_search(lst, predicate):
    """
    Find the left-most item in lst which obeys the given predicate
    """
    if not lst:
        return None

    low, high = 0, len(lst) - 1

    while low < high:
        lookup = (low + high) // 2
        if predicate(lst[lookup]):
            high = lookup
        else:
            low = lookup + 1

    return high if predicate(lst[high]) else None


def longest_increasing_subsequence(lst):
    """
    Given a list, find the longest increasing sub-sequence.

    Ex: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] → [0, 2, 6, 9, 11, 15]

    Time complexity: O(n log(n)) where n is the length of the list
    """
    solutions = [[]]

    for el in lst:
        idx = binary_search(solutions, lambda sol: sol[-1] > el if sol else False)

        if idx is None:
            solutions.append([solutions[-1], el])
        else:
            solutions[idx] = [solutions[idx-1], el]

    return flatten(solutions[-1])


print(longuest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))