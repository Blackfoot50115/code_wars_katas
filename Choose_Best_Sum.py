def choose_best_sum(t, k, ls):
    '''
        The function chooseBestSum (or choose_best_sum or ... depending on the language)
        will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns
        to visit, k >= 1) and ls (list of distances, all distances are positive or null integers
        and this list has at least one element). The function returns the "best" sum ie the biggest
        possible sum of k distances less than or equal to the given limit t, if that sum exists.

        Parameter rules:
            1.)t must be an int >= 0
            2.)k must be >= 1

        Algorithm:
            1.)Generate random summations of k items from ls --> summation_list
            2.)Pick largest item from summation_list that is <= t --> var_largest_summation
            3.)Return largest_summation

        Additional reading:
            -The following resource details unordered sampling without replacement
                https://www.probabilitycourse.com/chapter2/2_1_3_unordered_without_replacement.php
    '''

    from itertools import combinations

    # Create empty list to hold summations
    summations_list = []

    # Getting combinations(unordered sampling without replacement), convert to a list and store
    distances_list = list(combinations(ls, k))

    # Finds the summation of each sub-set in distances_list
    for i in distances_list:
        # i is a tuple, must convert to list data type before using sum()
        list(i)

        # Find the summation and add it to the summations_list
        summations_list.append(sum(i))

    # Filter out the summations that are larger than t
    qualifiers = [i for i in summations_list if i <= t]

    # Handle exception: qualifiers is empty
    if not qualifiers:
        exit()

    # Find the largest value in qualifiers
    largest_sum = max(qualifiers)

    return largest_sum
