def boyer(pattern, text):
    """
    Boyer-Moore algorithm
    """
    m = len(pattern)
    n = len(text)
    if m > n:
        return None
    skip = {}
    for k in range(256):
        skip[k] = m
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1
    k = m - 1
    while k < n:
        j = m - 1
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j < 0:
            return k + 1
        k += skip[text[k]]
    return None