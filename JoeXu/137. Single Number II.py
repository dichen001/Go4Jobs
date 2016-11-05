class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]=dict[nums[i]]+1
            else:
                dict[nums[i]]=1
        for ele in dict:
            if dict[ele]==1:
                return ele
"""                
here is another very good solution, this beat 99.08%, mine beat 88%:

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for i in range(len(A)):
            two |= A[i] & one              #two为1时，不管A[i]为什么，two都为1
            one = A[i] ^ one               #异或操作，都是1就进位
            three = ~(one & two)　　　　    #以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three
            two &= three
        return one


"""