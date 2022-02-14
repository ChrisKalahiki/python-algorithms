def linear_search(data, target):
    '''
    Linear Search Algorithm
    '''
    for index, item in enumerate(data):
        if item == target:
            return index
    return -1