class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def backtrack(i, cur, count):
            if i == n:
                cur += str(count) if count else ''
                ans.append(cur)
            else:
                backtrack(i+1, cur + str(count) + word[i] if count else cur + word[i], 0)
                backtrack(i+1, cur, count + 1)

        ans, n = [], len(word)
        backtrack(0,'',0)
        return ans

        n = len(word)
        ans = []
        for i in range(2**n):
            abbr = ''
            for j, c in enumerate(word):
                abbr += c if i & 2**j else '#'
            ans += [re.sub('#+', lambda x: str(len(x.group(0))), abbr)]
        return ans


s = Solution()
s.generateAbbreviations('word')
