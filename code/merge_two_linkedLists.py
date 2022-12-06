class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def merge_sorted_linked_lists(l1, l2):

    if l1 is None:
        return l2
    if l2 is None:
        return l1
    

    if l1.data <= l2.data:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    tail = head

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        
        tail = tail.next

    
    if l1 is not None:
        tail.next =  l1
    else:
        tail.next = l2
    
    return head