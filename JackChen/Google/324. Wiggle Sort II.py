class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        nums[::2], nums[1::2] = nums[:(n+1)/2][::-1], nums[(n+1)/2:][::-1]

        # O(n) solution
        
        # def A(i):
        #     n = len(nums)
        #     return (1+2*i) % (n | 1)
        # def median(lst):
        #     lst = sorted(lst)
        #     if len(lst) < 1:
        #             return None
        #     if len(lst) %2 == 1:
        #             return lst[((len(lst)+1)/2)-1]
        #     else:
        #             return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0
        # m = median(nums)
        # l, i, r = 0, 0, len(nums) - 1
        # while i <= r:
        #     if nums[A(i)] == m:
        #         i += 1
        #     elif nums[A(i)] > m:
        #         nums[A(i)], nums[A(l)] = nums[A(l)], nums[A(i)]
        #         i, l = i + 1, l + 1
        #     else:
        #         nums[A(i)], nums[A(r)] = nums[A(r)], nums[A(i)]
        #         r -= 1
                
                
                
        
            
