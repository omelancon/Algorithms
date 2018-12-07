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


def merge_many(*lsts):
    """
    Merge all items from k lists into one sorted list.

    Time complexity: O(n log(k)) where n is the total number of elements and k the number of lists
    """
    if not lsts:
        return []
    elif len(lsts) == 1:
        return lsts[0][:]
    elif len(lsts) == 2:
        return merge(*lsts)
    else:
        left = lsts[len(lsts) // 2:]
        right = lsts[:len(lsts) // 2]

        return merge(merge_many(*left), merge_many(*right))


def timsort(lst):
    """
    Timsort is an improved version of Merge Sort which splits the list into monotonic sub-lists before merging them
    into a sorted list.

    Worst case time complexity: O(n log(n))
    Best cast time complexity:  O(n) when the list is almost sorted
        where n is the number of elements in the list
    """
    sublsts = []

    i = 0
    while i < len(lst):
        sublsts.append([lst[i]])
        i += 1

        if i < len(lst) and lst[i] >= lst[i - 1]:
            while i < len(lst) and lst[i] >= lst[i - 1]:
                sublsts[-1].append(lst[i])
                i += 1
        elif i < len(lst):
            while i < len(lst) and lst[i] < lst[i - 1]:
                sublsts[-1].append(lst[i])
                i += 1

            sublsts[-1] = sublsts[-1][::-1]

    return merge_many(*sublsts)