"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lists = []
        for i in range(numRows):
            lists.append([1]*(i+1))
            if i > 1:
                for j in range(1,i):
                    lists[i][j] = lists[i-1][j-1] + lists[i-1][j]
        return lists

"""
found a brilliant solusion!

def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]

explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0
 +  0 1 3 3 1
 =  1 4 6 4 1
"""
