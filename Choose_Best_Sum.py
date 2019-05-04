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
            -The following resource details
    '''

    from itertools import combinations

    distances_list = list(combinations(ls, k))
    summations_list = []

    for i in distances_list:
        list(i)
        total_distance = sum(i)
        summations_list.append(total_distance)

    qualifiers = [i for i in summations_list if i <= t]
    if not qualifiers:
        exit()
    largest_sum = max(qualifiers)
    return largest_sum


# Just used for testing the function
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

best_sum = choose_best_sum(400, 3, xs)
print(best_sum)
