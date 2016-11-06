"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, 4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if len(s) - k > 3 or len(s) - k < 1:
                        continue
                    s1, s2, s3, s4 = s[0:i], s[i:j], s[j:k], s[k:]
                    if self.isvalid(s1) and self.isvalid(s2) and self.isvalid(s3) and self.isvalid(s4):
                        result.append('.'.join([s1,s2,s3,s4]))
        return result

    def isvalid(self, s):
        if (s[0] == '0' and len(s) > 1) or int(s) > 255:
            return False
        return True



s = Solution()
s.restoreIpAddresses('1111')
