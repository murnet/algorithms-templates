class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def reverse_list(node):
    temp = None

    while node is not None:
        temp = node.prev
        node.prev = node.next
        node.next = temp
        node = node.prev

    if temp is not None:
        node = temp.prev
    return node


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


if __name__ == '__main__':
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    new_head = reverse_list(node0)
    print_linked_list(new_head)
