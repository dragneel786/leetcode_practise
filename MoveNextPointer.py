def connect(root):
    node = root

    while(node.left):
        head = node
        while(head):
            head.left.next = head.right
            if(head.next != None):
                head.right.next = head.next.left
            head = head.next
        
        node = node.left