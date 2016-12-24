"""
Given a string, sort it in decreasing order based on the frequency of characters.
Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        bucket = [''] * (len(s) + 1)
        for c, n in freq.iteritems():
            bucket[n] += n * c
        ans = []
        for i in range(len(s) + 1)[::-1]:
            if bucket[i]:
                ans.append(bucket[i])
        return ''.join(ans)



        # O(nlog(n))
        freq = [[0,''] for _ in range(128)]
        for c in s:
            freq[ord(c)][0] += 1
            freq[ord(c)][1] = c
        return ''.join([item[1] * item[0] for item in sorted(freq, reverse= True) if item[0] > 0])
