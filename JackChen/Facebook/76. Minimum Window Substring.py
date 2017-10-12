"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""



import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        missing, need = len(t), collections.Counter(t)
        i = l = r = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not r or j - i <= r - l:
                    l, r = i, j
        return s[l:r]


#         def get_all(counter):
#             for c, cnt in counter.iteritems():
#                 if cnt > 0:
#                     return False
#             return True

#         needs, pos, ans = collections.Counter(t), collections.defaultdict(collections.deque), s + 'x'
#         for i, c in enumerate(s):
#             if c in needs:
#                 needs[c] -= 1
#                 pos[c].append(i)
#                 if needs[c] < 0:
#                     pos[c].popleft()
#             if get_all(needs):
#                 l = min([p[0] for p in pos.values()])
#                 h = max([p[-1] for p in pos.values()])
#                 if h - l + 1 < len(ans):
#                     ans = s[l:h+1]
#         return ans if len(ans) <= len(s) else ""


s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
