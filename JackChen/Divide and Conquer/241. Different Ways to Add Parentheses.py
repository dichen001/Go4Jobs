"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[0::2])
        operators = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get,tokens[1::2])
        low, high = 0, len(nums) - 1
        def divide(low, high):
            if low == high:
                return [nums[low]]
            # part = []
            # for i in range(low, high):
            #     for a in divide(low, i):
            #         for b in divide(i+1, high):
            #             part.append(operators[i](a,b))
                        # if operators[i] == '+':
                        #     part.append(a + b)
                        # elif operators[i] == '-':
                        #     part.append(a - b)
                        # else:
                        #     part.append(a * b)
            # return part
            return [operators[i](a,b) for i in range(low, high)
                                        for a in divide(low, i)
                                            for b in divide(i+1, high)]
        return divide(0, high)
