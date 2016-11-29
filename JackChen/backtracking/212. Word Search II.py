class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        root = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(root, map(list, board), i, j, result)
        return result

    def buildTrie(self, words):
        root = {}
        for word in words:
            p = root
            for c in word:
                if not p.get(c):
                    p[c] = {}
                p = p[c]
            p['end'] = word
        return root

    def dfs(self, root, board, i, j, result):
        if root.get('end'):
            result.append(root['end'])
            root['end'] = None
        if i in [-1, len(board)] or j in [-1, len(board[0])] or board[i][j] == '#' or not root.get(board[i][j]):
            return
        c = board[i][j]
        board[i][j] = '#'
        self.dfs(root[c], board, i-1, j, result)
        self.dfs(root[c], board, i+1, j, result)
        self.dfs(root[c], board, i, j-1, result)
        self.dfs(root[c], board, i, j+1, result)
        board[i][j] = c


s = Solution()
a = s.findWords(["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"])

print a
