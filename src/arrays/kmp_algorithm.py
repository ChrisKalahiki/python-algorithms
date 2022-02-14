def kmp_search(text, pattern):
    """
    KMP algorithm
    """
    # Create the table
    table = [0] * (len(pattern) + 1)
    table[0] = -1
    k = -1
    for i in range(1, len(pattern)):
        while k >= 0 and pattern[k + 1] != pattern[i]:
            k = table[k]
        if pattern[k + 1] == pattern[i]:
            k += 1
        table[i] = k
    # Search
    k = -1
    for i in range(len(text)):
        while k >= 0 and pattern[k + 1] != text[i]:
            k = table[k]
        if pattern[k + 1] == text[i]:
            k += 1
        if k == len(pattern) - 1:
            print("Pattern found at index {}".format(i - k))
            k = table[k]
            