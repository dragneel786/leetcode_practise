def mergeTrees(root1, root2):
    if (not root1 and not root2):
        return None
    
    newNode = TreeNode()
    if (not root1 and root2):
        newNode.val = root2.val
    
    elif (root1 and not root2):
        newNode.val = root1.val
    
    else:
        newNode.val = root1.val + root2.val
    
    newNode.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    newNode.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return newNode

