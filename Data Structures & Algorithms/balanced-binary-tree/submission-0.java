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
    public boolean bool;
    public boolean isBalanced(TreeNode root) {
        this.bool = true;
        maxHeight(root);
        return this.bool;
    }
    public int maxHeight(TreeNode root){
        if(this.bool==false){
            return 0;
        }
        if(root==null){
            return 0;
        }
        int left = maxHeight(root.left)+1;
        int right = maxHeight(root.right)+1;
        if(Math.abs(left-right)>1){
            this.bool = false;
        }
        return Math.max(left,right);
    }
}
