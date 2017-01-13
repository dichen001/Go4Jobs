def substring(sub, string):
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

print substring('ABCDABD', 'ABC ABCDAB ABCDABCDABDE')