class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        def backtrack(cur, pos, cnt):
            if pos == len(word):
                ans.append(cur if cnt == 0 else cur + str(cnt))
            else:
                backtrack(cur, pos + 1, cnt + 1)
                backtrack(cur + ("" if cnt == 0 else str(cnt)) + word[pos], pos + 1, 0)

        ans = []
        backtrack("", 0, 0)
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
