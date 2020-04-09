from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: 'Node' = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def popFirst(self):
        old_head = self.head

        self.head = self.head.next
        self.size -= 1

        return old_head.value

    def reverse(self):
        reversed_list = LinkedList()

        head = self.head
        while head:
            reversed_list.append(head.value)
            head = head.next

        return reversed_list

    def __str__(self):
        values = []
        head = self.head
        while head:
            values.append(head.value)
            head = head.next
        return "->".join(str(s) for s in values)
        

def main():
    linked = LinkedList()
    linked.append(1)
    linked.append(2)
    linked.append(3)
    print(linked)

    reversed_list = linked.reverse()
    print(reversed_list)


if __name__ == "__main__":
    main()