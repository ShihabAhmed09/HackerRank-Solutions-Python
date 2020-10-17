class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next


def compare_lists(llist1, llist2):
    while llist1 and llist2:
        if llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return 1 if llist1 == llist2 else 0


# def compare_lists(llist1, llist2):
#     while llist1 or llist2:
#         if not (llist1 and llist2) or llist1.data != llist2.data:
#             return 0
#         llist1 = llist1.next
#         llist2 = llist2.next
#     return 1


# def compare_lists(llist1, llist2):
#     # repeat comparison until at least 1 pointer is null
#     while llist1 and llist2:
#         # fail on any inequality
#         if llist1.data != llist2.data:
#             return 0
#         # otherwise, point to next nodes
#         llist1, llist2 = llist1.next, llist2.next
#     # if both point to null, the lists are equal
#     if not (llist1 or llist2):
#         return 1
#     # if one pointer is not null, the lists are unequal length
#     return 0
# Time Complexity: O(N+M)


# def compare_lists(llist1, llist2):
#     if llist1 is None and llist2 is None:
#         return 1
#     elif llist1 is None or llist2 is None:
#         return 0
#
#     if llist1.data == llist2.data:
#         return compare_lists(llist1.next, llist2.next)
#     else:
#         return 0


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)
        print(result)
