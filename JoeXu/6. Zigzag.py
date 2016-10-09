class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if l<=numRows or numRows==1:
            return s
        final = [[] for row in xrange(numRows)]
        for i in range(len(s)): 
            final[numRows -1 - abs(numRows - 1 - i % (2 * numRows - 2))].append(s[i])
        return "".join(["".join(final[i]) for i in xrange(numRows)])
