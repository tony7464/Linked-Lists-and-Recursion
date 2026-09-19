class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        # Each node holds one ID and a pointer to the next node in the chain.
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    Recursion is used so each traversal step is a clear base case vs. recursive case.
    """

    def __init__(self):
        # An empty list starts with no head node.
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the front of the list in O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list in O(n) time."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        Return the sum of all node data using recursion.

        Recursion walks one node at a time: the base case is an empty
        remainder of the list (None), and the recursive case adds the
        current node's data to the sum of everything after it.
        """

        def _sum(node):
            # Base case: no more nodes, so this branch contributes 0.
            if node is None:
                return 0
            # Recursive case: current ID plus the sum of the rest of the list.
            return node.data + _sum(node.next)

        return _sum(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.

        Recursion is used to walk to the end, then re-point each node's
        next reference to the previous node on the way back conceptually
        by passing the previous node forward as we go.
        """

        def _reverse(prev, current):
            # Base case: we walked past the last node; prev is the new head.
            if current is None:
                return prev

            # Recursive case: save the next node, flip the pointer, continue.
            nxt = current.next
            current.next = prev
            return _reverse(current, nxt)

        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """
        Return True if target is found in the list, otherwise False.

        Recursion is used for a linear scan: stop at None (not found) or
        when the current node's data matches the target.
        """

        def _search(node):
            # Base case: reached the end without a match.
            if node is None:
                return False
            # Base case: the current node holds the target ID.
            if node.data == target:
                return True
            # Recursive case: keep looking in the remainder of the list.
            return _search(node.next)

        return _search(self.head)

    def display(self):
        """Print the list as 'val -> val -> ... -> None' for debugging."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        print(" -> ".join(values))
