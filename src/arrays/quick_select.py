def quick_select(arr, k):
    """
    Find the kth smallest element in an unsorted array.
    """
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    if k <= len(less):
        return quick_select(less, k)
    elif k > len(less) + 1:
        return quick_select(greater, k - len(less) - 1)
    else:
        return pivot