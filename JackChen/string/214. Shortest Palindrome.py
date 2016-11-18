"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP
        l = s + '#' + s[::-1]
        table = [0] * len(l)
        for i in range(1, len(l)):
            matched = table[i-1]
            while matched > 0 and l[i] != l[matched]:
                matched = table[matched-1]
            if l[i] == l[matched]:
                matched += 1
            table[i] = matched
        return s[table[-1]:][::-1] + s


        ## Brute Force: Theirs, somehow passed.
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
        ## Brute Force: Mine, somehow TLF and MLE.. WHT!
        max = 1
        for pos in range((len(s)+1)/2-1, 0, -1):
            if s[0:pos+1] == s[pos:2*pos+1][::-1]:
                max = 2*pos + 1
                break
            if s[0:pos] == s[pos:2*pos][::-1]:
                max = 2*pos
                break
        return s[max:][::-1] + s if s[max:] else s





