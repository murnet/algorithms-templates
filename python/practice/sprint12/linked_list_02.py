class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedListNode(value, self.head)

    def insert(self, index, value):
        if self.head is None:
            self.head = LinkedListNode(value, None)
        elif index == 0:
            self.add(value)
        else:
            current = self.head
            while current.next is not None and index > 0:
                current = current.next
                index = index - 1

            current.next = LinkedListNode(value, current.next)


if __name__ == '__main__':
    head = LinkedListNode(
        5, LinkedListNode(8, LinkedListNode(12, LinkedListNode(3, None)))
    )
    # print(_head)
