def a2A(s):
    """
    Given 'ab' get all combination of 'ab', 'Ab', 'aB', 'AB'
    :param s:
    :return:
    """
    def dfs(S, start):
        ans.append("".join(S))
        for i, c in enumerate(S[start:], start):
            S[i] = c.upper()
            dfs(S, i+1)
            S[i] = c

    ans = []
    dfs([c for c in s], 0)
    return ans

print a2A("a")
print a2A("ab")
print a2A("abc")
