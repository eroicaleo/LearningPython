import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeBuilder(nodeString):
    nodeList = nodeString[1:-1].split(',')
    nodeQueue = queue.Queue()
    root = TreeNode(int(nodeList[0]))
    currNode = root
    leftDone, rightDone = 0, 0
    for val in nodeList[1:]:
        print('processing %s' % val)
        print('leftDone,', leftDone, 'rightDone,', rightDone)
        if val != 'null':
            newNode = TreeNode(int(val))
            print("create new node: %d" % newNode.val)
            nodeQueue.put(newNode)
        else:
            newNode = None

        if leftDone == 0:
            currNode.left, leftDone = newNode, 1
        elif rightDone == 0:
            currNode.right, rightDone = newNode, 1
            leftDone, rightDone = 0, 0
            currNode = nodeQueue.get()
    return root

def traverse(node):
    print('Node: %d' % node.val)
    if node.left != None:
        print('Left: %d' % node.left.val)
    if node.right != None:
        print('Right: %d' % node.right.val)
    if node.left != None:
        traverse(node.left)
    if node.right != None:
        traverse(node.right)

class Solution:
    def __init__(self):
        self.prev = None
        self.head = None
        self.tail = None
        self.max  = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dualNode(root)
        self.head.val, self.tail.val = self.tail.val, self.head.val

    def dualNode(self, node):
        if node == None:
            return
        self.dualNode(node.left)
        if self.prev != None:
            if self.head == None and self.prev.val > node.val:
                self.head = self.prev
        self.prev = node
        if self.max == None or node.val > self.max:
            self.max = node.val
        if node.val < self.max:
            self.tail = node
        self.dualNode(node.right)

sol = Solution()
nodeString = '[1,3,null,null,2]'
nodeString = '[3,1,4,null,null,2]'
nodeString = '[3,null,2,null,1]'
nodeString = '[2,3,1]'
root = treeBuilder(nodeString)
traverse(root)
sol.dualNode(root)
print(sol.head.val, sol.tail.val)
sol.recoverTree(root)
