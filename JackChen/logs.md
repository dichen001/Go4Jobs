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
