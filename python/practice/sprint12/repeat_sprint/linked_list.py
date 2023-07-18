class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

    def __repr__(self):
        return self.value


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next_item
    print("None")


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next_item = head
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next_item = previous_node.next_item
    previous_node.next_item = new_node
    return head


def delete_node(head, index):
    if index == 0:



if __name__ == '__main__':
    n3 = Node('node3')
    n2 = Node('node2', n3)
    n1 = Node('node1', n2)
    n0 = Node('node0', n1)
