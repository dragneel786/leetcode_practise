def removeNthFromEnd(self, head, n):
    first = head
    second = head
    
    for i in range(n - 1):
        if not first.next:
            break
        first = first.next
    
    prev = None
    while(first.next):
        first = first.next
        prev = second
        second = second.next
        
    if(second == head):
        head = head.next
    else:
        prev.next = second.next
    
    print(head)