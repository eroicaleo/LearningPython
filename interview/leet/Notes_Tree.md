
# Some tricks in tree problem

## Max path sum problem

* It's useful to keep a max instance variable to make code cleaner
    * E.g.: `124_Binary_Tree_Maximum_Path_Sum_v3.py`
    * E.g.: `543_Diameter_of_Binary_Tree.py`

# preorder iterative

# inorder iterative

# postorder iterative

# Build tree from preorder travel

* `1008_Construct_Binary_Search_Tree_from_Preorder_Traversal.py`

```python
    def bstFromPreorder_lee315(self, preorder):
        ix, l = 0, len(preorder)
        def dfs(ub):
            if ix >= l or preorder[ix] > ub:
                return None
            root, ix = TreeNode(preorder[ix]), ix+1
            root.left = dfs(root.val)
            root.right = dfs(ub)
        return dfs(None)

    def bstFromPreorder_bfs(self, preorder):
        stack = [TreeNode(math.inf)]
        for n in preorder:
            node, prev = TreeNode(n), stack[-1]
            if prev.val > n:
                prev.left = node
            else:
                while n > prev.val:
                    prev = stack.pop()
                prev.right = node
            stack.append(node)
        return stack[0].left
```

# Build tree from preorder inorder traval
