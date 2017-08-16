"""
KMP searches for occurrences of a "word" W within a main "text string" S.
"""


def substring(sub, string):
    """
    Assuming the prior existence of the table T,
    the search portion of the KMP algorithm has complexity O(n),
    where n is the length of S and the O is big-O notation.
    :param sub:
    :param string:
    :return:
    """
    T = buildKMP(sub)
    # m is the beginning of current match in string
    # i is the position of the current char in substring
    m, i = 0, 0
    n = len(string)
    while m + i < n:
        if sub[i] == string[m+i]:
            if i == len(sub) - 1:
                return (m, m+i, string[m:m+i+1])
            i += 1
        elif i == 0:
            m += 1
        else:
            m = m + i - T[i]
            i = T[i]
    return (m, m+i, string[m:m+i+1])



def buildKMP(s):
    """
    The complexity of the table algorithm is O(k), where k is the length of W
    :param s:
    :return:
    """
    l, r = 0, 1
    n = len(s)
    # T[i+1] stores maximum number of characters that the string is repeating itself up to position i.

    T = [0] * (n+1)
    while r < n:
        if s[l] == s[r]:
            T[r+1] = l + 1
            l += 1
            r += 1
        elif l == 0:
            r += 1
        else:
            l = T[l]
    return T

print substring('aacaacXaacaac', 'ABC ABCDAB ABCDABCDABDE')