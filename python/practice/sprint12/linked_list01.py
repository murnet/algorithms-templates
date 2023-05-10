class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index - 1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


def delete_node(head, index):
    if index == 0:
        if head is None:
            return None
        else:
            return head.next

    previous_node = get_node_by_index(head, index - 1)
    if previous_node is None or previous_node.next is None:
        return head

    previous_node.next = previous_node.next.next
    return head


def get_index(node, value):
    index = 0
    while node is not None:
        if node.value == value:
            return index
        node = node.next
        index += 1
    return -1


if __name__ == '__main__':
    # n5 = Node('fifth')
    # n4 = Node('fourth', n5)
    # n3 = Node('third', n4)
    # n2 = Node('second', n3)
    # n1 = Node('first', n2)
    # print_linked_list(n1)
    # print_linked_list(n3)
    # node, index, value = n1, 2, 'new_node'
    # head = insert_node(node, index, value)
    # print_linked_list(head)
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    # print_linked_list(node0)
    # insert_node(node0, 1, 'new_node')
    # print_linked_list(node0)
    # delete_node(node0, 2)
    # print_linked_list(node0)
    print(get_index(node0, 'node0'))
