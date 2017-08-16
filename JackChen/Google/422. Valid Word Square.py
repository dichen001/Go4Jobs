
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words or not words[0] or len(words) != len(words[0]):
            return False
        l = len(words[0])
        words = [w + '*' * (l-len(w)) for w in words]
        wordsT = zip(*words)
        for i, w in enumerate(words):
            if w != ''.join(wordsT[i]):
                return False
        return True


s = Solution()
s.validWordSquare(["abcd","bnrt","crmy","dtye"])

