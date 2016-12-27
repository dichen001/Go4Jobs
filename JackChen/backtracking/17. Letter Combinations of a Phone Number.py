"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backtrack(start, cur, n):
            if start == n:
                ans.append(''.join(cur))
            else:
                for c in map[digits[start]]:
                    backtrack(start+1, cur + [c], n)
        map = { '2': 'abc', '3': 'def',\
                '4': 'ghi', '5': 'jkl', '6': 'mno', \
                '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        backtrack(0, [], len(digits))
        return ans if digits else []

