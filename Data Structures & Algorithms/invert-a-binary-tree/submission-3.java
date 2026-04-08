/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode invertTree(TreeNode root) {
        //case 1: no children -> do nothing
        //case 2: 1 child -> switch pointers
        //case 3: 2 children -> switch pointers

        if(root == null) return root;

        if(root.left != null) {
            invertTree(root.left);
            
        }
        if(root.right != null) {
            invertTree(root.right);
        }

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

       

        return root;
    }
}
