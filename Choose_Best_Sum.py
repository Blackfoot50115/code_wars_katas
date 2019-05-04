def choose_best_sum(t, k, ls):
    '''
        The function chooseBestSum (or choose_best_sum or ... depending on the language)
        will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns
        to visit, k >= 1) and ls (list of distances, all distances are positive or null integers
        and this list has at least one element). The function returns the "best" sum ie the biggest
        possible sum of k distances less than or equal to the given limit t, if that sum exists,

        List of Distances xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

        Parameter rules:
            1.)t must be an int >= 0
            2.)k must be >= 1

        Algorithm:
            1.)Generate random summations of k items from ls without creating pairs --> summation_list
            3.)Pick largest item from summation_list that is <= t --> var_largest_summation
            4.)Return largest_summation
    '''

