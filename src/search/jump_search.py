def jump_search(data, target):
    '''
    Jump Search Algorithm
    '''
    step = int(len(data) ** 0.5)
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = low + step
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1