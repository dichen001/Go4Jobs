class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # BFS topological
        #  sort
        chars = set(''.join(words))
        graph = {c:set() for c in chars}
        in_degree = {c:0 for c in chars}
        flag = False
        for pair in zip(words[:-1], words[1:]):
            if len(pair[0]) > len(pair[1]):
                flag = True
            for a, b in zip(*pair):
                if a != b:
                    graph[a].add(b)
                    in_degree[b] += 1
                    break
        queue = [c for c in chars if in_degree[c] == 0]
        if len(queue) == len(chars) and flag:
            return ''
        ans = ''
        while queue:
            c = queue.pop(0)
            ans += c
            for cc in graph[c]:
                in_degree[cc] -= 1
                if in_degree[cc] == 0:
                    queue.append(cc)
        return ans if len(ans) == len(chars) else ''



s = Solution()
s.alienOrder(["za","zb","ca","cb"])
