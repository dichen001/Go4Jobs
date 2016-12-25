class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # binary search version
        def biSearch(lo, hi, check):
            while lo < hi:
                mid = (lo + hi) / 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        m, n = len(image), len(image[0])
        imageT = zip(*image)
        left = biSearch(0, x, lambda x: '1' in imageT[x])
        right = biSearch(x, n, lambda x: '1' not in imageT[x])
        up = biSearch(0, x, lambda x: '1' in image[x])
        down = biSearch(x, m, lambda x: '1' not in image[x])
        return (down - up) * (right - left)


        # much slower version

        def dfs(i,j, m, n):
            if i < 0 or i >=m or j < 0 or j >=n or image[i][j] == '0' or (i,j) in visited:
                return
            visited.add((i,j))
            if j < border[0]: border[0] = j
            if j > border[1]: border[1] = j
            if i < border[2]: border[2] = i
            if i > border[3]: border[3] = i
            dfs(i, j+1, m, n)
            dfs(i, j-1, m, n)
            dfs(i+1, j, m, n)
            dfs(i-1, j, m, n)

        if not image or not image[0]:
            return 0
        m, n = len(image), len(image[0])
        #           l, r, u, d
        border = [n, 0, m, 0]
        visited = set()
        dfs(x,y,m,n)
        return (border[1] - border[0] + 1) * (border[3] - border[2] + 1)


s = Solution()
s.minArea(["0010","0110","0100"], 0, 2)
