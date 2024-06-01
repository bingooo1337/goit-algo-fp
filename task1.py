from __future__ import annotations


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            prev = cur
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        output = "["
        current = self.head
        while current:
            output += f"{current.data}, "
            current = current.next
        output = output.removesuffix(", ")
        output += "]"
        print(output)

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # insertion sort
    def sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.__sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    def merge_sorted_lists(self, list1: LinkedList, list2: LinkedList):
        head1 = list1.head
        head2 = list2.head

        dummy = Node()
        tail = dummy

        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 if head1 else head2

        return dummy.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end("12")
    linked_list.insert_at_end("53")
    linked_list.insert_at_end("23")
    linked_list.insert_at_end("57")
    linked_list.insert_at_end("34")

    print("LinkedList")
    linked_list.print_list()
    print()

    linked_list.sort()
    print("Sorted LinkedList")
    linked_list.print_list()
    print()

    linked_list.reverse_list()
    print("Reversed LinkedList")
    linked_list.print_list()
    print()

    linked_list.reverse_list()
    linked_list1 = linked_list
    print("LinkedList1")
    linked_list1.print_list()

    linked_list2 = LinkedList()
    linked_list2.insert_at_end("1")
    linked_list2.insert_at_end("13")
    linked_list2.insert_at_end("55")
    linked_list2.insert_at_end("60")
    print("LinkedList2")
    linked_list2.print_list()

    merged_list = LinkedList()
    merged_list.head = merged_list.merge_sorted_lists(
        linked_list1,
        linked_list2
    )

    print("Merged sorted LinkedList1 and sorted LinkedList2")
    merged_list.print_list()
