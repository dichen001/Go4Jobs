# Longest Increasing Subsequence.
# Basic DP.

M =[[1,     2,     3,     4],
    [5,     6,     7,    8],
    [9,    10,    11,    12],
    [13,   14,    15,    16],
    [17,   18,    19,    20]]

m, n = len(M), len(M[0])
for k in range(m + n - 1):
    i = min(k, m - 1)
    j = max(0, k - m + 1)
    tmp = []
    while 0 <= i and j < n:
        tmp += [str(M[i][j])]
        i, j = i-1, j + 1
    print ' '.join(tmp)

