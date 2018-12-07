def merge(l1, l2):
    """
    Merge all items from two sorted list into one sorted list.

    Time complexity: O(n) where n is the total number of elements
    """
    i = j = 0
    output = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            output.append(l1[i])
            i += 1
        else:
            output.append(l2[j])
            j += 1

    output.extend(l1[i:] + l2[j:])

    return output


def mergesort(lst):
    """
    Sorts a list by breaking it down into sub-lists of size 0 or 1 and merging them back to a sorted list.
    Merge Sort uses the fact that a list of size 0 or 1 is necessarily sorted.

    Time complexity: O(n log(n)) where n is the number of elements in the list
    """
    if len(lst) <= 1:
        return lst[:]
    else:
        middle = len(lst) // 2
        left = mergesort(lst[:middle])
        right = mergesort(lst[middle:])

        return merge(left, right)