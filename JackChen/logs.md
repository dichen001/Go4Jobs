## 09/20/16     

Begin with Arrary. ` +3(1*, 27, 189), now 3/77.`

Abondon previous progresses on Leetcode and start a new session.


#### 1. Two Sum -- Trade Space for Time
My first try uses 2 while loop, whose time complexity is o(N^2), but got **"Time Limit Exceeded"**.
Then I realize, for integers, without the limit for space usage, we can easily achieve o(N) time comlexity with o(N) space complexity.
OK. Do remember this trick for INTEGERS. Same idea behind **Count Search**.


------------
## 09/21/16
`+4 (217, 219, 283, 396*)`

#### 396. Rotate Function -- Math matters...
Finding the fomula changes O(N^2) to O(N) 

------------
## 09/22/16
`+5 (26, 66, 118, 119, 121)`

#### 118/119. Pascal's Triangle -- Math is Magical!
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```
```
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
```

explanation: Any row can be constructed using the offset sum of the previous row. Example:
```
    1 3 3 1 0
 +  0 1 3 3 1
 =  1 4 6 4 1
```

------------
## 09/23/16
`+5 (64, 88, 162, 169, 402*)`

#### 402. Remove K Digits -- Stack!

------------
## 09/24/16
`+1 (122)`

#### 122. Best Time to Buy and Sell Stock II -- Local and global maximum.

------------
## 09/25/16
`+3 (152, 153, 289)`

#### 152. Maximum Product Subarray -- Local and global maximum.

------------
## 09/26/16
`+4 (90, 120*, 238*, 268)`

#### 120. Triangle  -- DP! Bottom-Up!
#### 238. Product of Array Except Self! -- 摇摆！摇摆！左右摇摆！

------------
## 09/27/16
:zzz::zzz::zzz::zzz::zzz::zzz:


------------
## 09/28/16
`+4 (78, 79*, 80*, 229)`

#### 78. Subsets. -- The solustion could be so CONCISE!
#### 79. Word Search -- DFS. Wow!


------------
## 09/29/16
`+4 (74, 75*, 105*, 106*)`

#### 74. Search a 2D Matrix. -- Treat it as 1D !!!
#### 105-106. Constract binary Tree from Inorder and Postoder/Preoder Traversal!  淫吹思婷！

------------
## 09/30/16
`+6 (33, 62-63*, 73*, 81, 228, )`

#### 62-63. Unique paths. --- Wow! Dynamic Programming, find recurrsions. Trick for save Space. 
#### 73. Set Matrix Zeroes. --- Constant space constrains! Directly use the matrix itself as storage!! 逸渴塞挺！



------------
## 10/01/16
`+1 (209)`

------------
## 10/02/16
`+1 (53)`

------------
## 10/03/16
`+3 (39, 50, 216)`

All about Combination Sum I,II,III.

------------
## 10/04/16
`+4 (48, 54, 59, 167)`

48, 54, 59 are all about matrix.
#### 48. Rotate Imate.  --- Pay attention to the iteration range for transpose(`i in range(n); j in range(i+1,n)` and reverse(`i in range(n); j in range(n/2)`).


------------
## 10/05/16
`+6 (15, 16, 18, 34, 35, 55)`
#### n-Sum Question -- 1,15,16,18 are all about the same idea.
Tansform N-sum into 2-sum, then use bi-direction search on sorted array, which is O(n)time and O(1) space.


------------
## 10/09/16
`+4 (22, 24, 299, 409)`
#### Count Primes
O(N*log(log(N))) time, O(N) space. 

------------
## 10/13/16
`+4 (94, 166, 347)`
#### Binary Tree Inorder Traversal
Should familar with recursive and iterative solusions.
#### Top K Frequent Elements
Application of Bucket Sort. When n number in range(n). Use O(n) space to make O(nlog(n)) time to O(n) time.

------------
## 10/14/16
`+8 (19, 21, 24, 83, 141, 206, 234, 237)`
#### Remove Nth Node From End of List
2 pointers. faster one move N time first. Then move slow and fast together till fast reach end.

------------
## 10/15/16
`+6 (83, 92**, 142, 143, 160*, 203)`

------------
## 10/16/16
`+6 (2, 61, 82, 86, 109*, 328)`

------------
## 10/17/16
`+6 (13, 147*，148*, 171, 258, 415)`

------------
## 10/18/16
`+7 (7, 8, 9, 172, 263, 326, 400)`

------------
## 10/19/16
`+5 (12, 67, 168, 223, 231)`

------------
## 10/20/16
`+4 (43, 60, 264, 397)`


------------
## 11/01/16
`69. Sqrt(x)`
```
# newton's methods:
    # f(x) = r^2 - x = 0
    # x(i+1) = x(i) - f(x(i))/f'(x(i))
```


------------
## 11/02/16

`365. Water and Jug Problem`
```
GCD - Greatest Common Divisor
def GCD(x, y):
    while y != 0:
        t = y
        y = x % y
        x = t
    return x
```


------------
## 11/05/16
How you see a problem matters. Note to change a direction of view.
`5*, 91*`

------------
## 11/06/16
collections.defaultdict(set)


------------
## 11/07/16
做 Hard 太尼玛酸爽啦


------------
## 12/14/16
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters
340. Longest Substring with At Most K Distinct Characters
30. Substring with Concatenation of All Words
76. Minimum Window Substring
209. Minimum Size Subarray Sum
239. Sliding Window Maximum



## Backtracking Summary

Backtrack Summary: General Solution for 10 Questions!!!!!!!! Python (Combination Sum, Subsets, Permutation,  Palindrome)

For Java version, please refer to [isssac3's answer.](https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning)

**39. Combination Sum**
https://leetcode.com/problems/combination-sum/
```
    def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = [] 
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans
```

**40. Combination Sum II**
https://leetcode.com/problems/combination-sum-ii/
```
    def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        return ans
```

**78. Subsets**
https://leetcode.com/problems/subsets/
```
    def subsets(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans
```

**90. Subsets II**
https://leetcode.com/problems/subsets-ii/
```
    def subsetsWithDup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans
```

**46. Permutations**
https://leetcode.com/problems/permutations/
```
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        return ans
```

**47. Permutations II**
https://leetcode.com/problems/permutations-ii/
```
    def permuteUnique(self, nums):
        def backtrack(tmp, size):
            if len(tmp) == size:
                ans.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False
        ans = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack([], len(nums))
        return ans
```

**60. Permutation Sequence**
https://leetcode.com/problems/permutation-sequence/
```
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n+1)]
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k / fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans)
```

**131. Palindrome Partitioning**
https://leetcode.com/problems/palindrome-partitioning/
```
    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans
```

****


**267. Palindrome Permutation II**
https://leetcode.com/problems/palindrome-permutation-ii/
Related to this two:
`31. Next Permutation`: https://leetcode.com/problems/next-permutation/
`266. Palindrome Permutation`: https://leetcode.com/problems/palindrome-permutation/

```
    def generatePalindromes(self, s):
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v%2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v/2) for k, v in kv.iteritems()])
        half = [c for c in half]
        
        def backtrack(end, tmp):
            if len(tmp) == end:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i>0 and half[i] == half[i-1] and not visited[i-1]):
                        continue
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(end, tmp)
                    visited[i] = False
                    tmp.pop()
                    
        ans = []
        visited = [False] * len(half)
        backtrack(len(half), [])
        return ans
```


