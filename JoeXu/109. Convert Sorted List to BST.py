# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
            l=len(nums)
            if l==0:
                return None
            elif l==1:
                return TreeNode(nums[0])
            else:
                root=TreeNode(nums[l//2])
                root.left=self.sortedArrayToBST(nums[:l//2])
                root.right=self.sortedArrayToBST(nums[l//2+1:])
                return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums=[]
        point=head
        while point!=None:
            nums.append(point.val)
            point=point.next
        return self.sortedArrayToBST(nums)