class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable.
        Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """

        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list recursively.
        """

        def helper(prev, current):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev

            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        Search for a target value recursively.
        """

        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        Display the linked list.
        """
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        values.append("None")
        print(" -> ".join(values))