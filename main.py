def remove(self, data):
    if self.head is None:
        return

    if self.head.data == data:
        self.head = self.head.next
        return

    current = self.head
    prev = None

    while current:
        if current.data == data:
            prev.next = current.next
            return
        prev = current
        current = current.next