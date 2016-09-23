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

#### 118/119 Pascal's Triangle -- Math is Magical!
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
