import timeit
class Solution(object):
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        kvmaps = {
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }


        # iterative fastest
        ans = [""]
        for d in digits:
            tmp = []
            for c in kvmaps[d]:
                for a in ans:
                    tmp.append(a + c)
            ans = tmp
        return ans if digits else []


        # iterative slower
        ans = [[]]
        for d in digits:
            tmp = []
            for c in kvmaps[d]:
                for a in ans:
                    tmp.append(a + [c])
            ans = tmp
        return map(lambda a: "".join(a), ans) if digits else []


        # recursive
        ans = [[]]
        def dfs(pre, left):
            if not left:
                ans.append("".join(pre))
                return
            for c in kvmaps[left[0]]:
                dfs(pre + [c], left[1:])
        dfs([], digits)
        return ans if digits else []


s = Solution()
i = "12345678923"
k = 1

t0 = timeit.default_timer()
for _ in range(k):
    s.letterCombinations3(i)
t1 = timeit.default_timer()
print t1 - t0

t0 = timeit.default_timer()
for _ in range(k):
    s.letterCombinations2(i)
t1 = timeit.default_timer()
print t1 - t0

t0 = timeit.default_timer()
for _ in range(k):
    s.letterCombinations1(i)
t1 = timeit.default_timer()
print t1 - t0





print "done"