from operator import itemgetter

def knapsack(capacity, items, weight_getter=itemgetter(0), value_getter=itemgetter(1)):
    """
    Given a set of items each having an associated weight and value, and a maximum capacity, find the combination of
    items which sum of weight is below the maximum capacity and sum of values is the greatest.

    The dynamic programming algorithm builds up to the solution for capacities 0 to 'capacity' using the relation:

    solutions[0] = No item (value=0)
    solutions[k] = max(solutions[k-weight_i] + value_i for each i in items)

    Time complexity: O(n * c) where n is the number of items and c the maximum capacity.
        assuming the weight_getter and value_getter are both O(1)
    """
    solutions = [(0, None)] * (capacity + 1)

    # Recursively choose the best item for each step
    for i in range(capacity + 1):
        for item in items:
            weight, value = weight_getter(item), value_getter(item)

            if weight <= i:
                new_value = solutions[i - weight][0] + value
                if new_value > solutions[i][0]:
                    solutions[i] = new_value, item

    # Build the best solution from the steps
    best = []
    item = solutions[capacity][1]
    while item is not None:
        best.append(item)
        capacity -= weight_getter(item)
        item = solutions[capacity][1]

    return best
