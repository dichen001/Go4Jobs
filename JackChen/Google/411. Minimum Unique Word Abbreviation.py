class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def code(w):
            n = len(w)
            for k in range(n+1, 0, -1):
                for i in range(n-k+1):
                    key = w[0:n-k-i] + str(k) + w[n-i:]
                    if not dic.get(key):
                        dic[key] = w
                        return key
            dic[w] = w
            return w

        dic = {}
        for w in dictionary:
            code(w)
        return code(target)

s = Solution()
s.minAbbreviation("apple", ["blade","plain","amber"])
