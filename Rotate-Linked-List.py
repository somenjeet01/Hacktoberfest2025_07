def rotateRight(head, k):
    if not head or not head.next:
        return head
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1
    tail.next = head
    k = k % length
    steps = length - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
