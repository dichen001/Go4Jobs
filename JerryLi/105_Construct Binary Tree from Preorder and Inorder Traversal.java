/*
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
	/*
	Solution in Discussion:
	The the basic idea is to take the first element in preorder array as the root, find the position of the root in the inorder array; then locate the range for left sub-tree and right sub-tree and do recursion.
	*/
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> indices = new HashMap<>(); // <value, index> in inorder array
        for (int i=0; i<inorder.length; i++) indices.put(inorder[i], i);
        
        return buildTree(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1, indices);
    }
    
    private TreeNode buildTree(int[] preorder, int pStart, int pEnd, int[] inorder, int iStart, int iEnd, Map<Integer,Integer> indices){
        if (pStart>pEnd || iStart>iEnd) return null;
        TreeNode root = new TreeNode(preorder[pStart++]);
        int iRoot = indices.get(root.val);
        int leftSize = iRoot - iStart;
        root.left = buildTree(preorder, pStart, pStart+leftSize-1, inorder, iStart, iRoot-1, indices);
        root.right = buildTree(preorder, pStart+leftSize, pEnd, inorder, iRoot+1, iEnd, indices);
        
        return root;
    }
}