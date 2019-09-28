# _*_coding:utf-8 _*_
# @Author　 : Ric

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        """
        :param root:TreeNode
        :param k:int
        :return:int
        """
        res = None

        def search(root):
            nonlocal k, res
            if root.left:
                search(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            if root.right:
                search(root.right)

        search(root)
        return res
