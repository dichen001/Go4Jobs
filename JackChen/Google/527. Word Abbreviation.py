"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

"""

import collections
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """

        def getCommonPrefix(w1, w2):
            for i, c in enumerate(w1):
                if c != w2[i]:
                    return i
            return len(w1)

        ans, groups = [0] * len(dict), collections.defaultdict(list)
        for i, w in enumerate(dict):
            groups[(w[0], w[-1], len(w))].append((w, i))
        for (first, last, size), enums in groups.iteritems():
            enums.sort()
            # longest common prefix position
            lcp = [0] * len(enums)
            for i, (w1, _) in enumerate(enums):
                if i:
                    w0, _ = enums[i - 1]
                    p = getCommonPrefix(w0, w1)
                    lcp[i - 1] = max(lcp[i - 1], p)
                    lcp[i] = max(lcp[i], p)
            for (w, index), p in zip(enums, lcp):
                delta = size - p - 2
                if delta <= 1:
                    ans[index] = w
                else:
                    ans[index] = w[:p + 1] + str(delta) + last
        return ans


s = Solution()
s.wordsAbbreviation(["like","god","internal","me","internet","interval","intension","face","intrusion"])
