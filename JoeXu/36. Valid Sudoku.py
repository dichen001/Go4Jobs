ass Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r= [[] for i in range(9)]
        c= [[] for i in range(9)]
        grid= [[]for i in range(9)]
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e=='.':
                    continue
                if e in r[i]:
                    return False
                if e in c[j]:
                    return False
                r[i].append(e)
                c[j].append(e)
                
                k = i//3*3+j//3
                if e in grid[k]:
                    return False
                grid[k].append(e)
        return True
