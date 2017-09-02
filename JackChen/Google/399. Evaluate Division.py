"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build graph
        G = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            G[a][b], G[b][a] = v, 1.0 / v
            G[a][a], G[b][b] = 1.0, 1.0

        # dfs
        def dfs(s, e, visited):
            if e in G[s]:
                return G[s][e]
            for c in G[s].keys():
                if c not in visited:
                    v = dfs(c, e, visited | set(c))
                    if v != -1.0:
                        return G[s][c] * v
            return -1.0

        ans = []
        for s, e in queries:
            ans += [dfs(s, e, set(s))]
        return ans



s = Solution()
s.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
