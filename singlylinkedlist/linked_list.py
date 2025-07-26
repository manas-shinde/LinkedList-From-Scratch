from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, value: int):
        new_node: Node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value >= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous: Node = self.head
            runner: Node = self.head.next

            while runner is not None and value < runner.value:
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        e.g., "1 -> 2 -> 3 -> None"
        """
        result: str = ""
        runner_node: Node = self.head

        # Handle the case of an empty list
        if runner_node is None:
            return "None"

        # Traverse the list and build the string
        while runner_node is not None:
            result += str(runner_node.value)
            if runner_node.next is not None:
                result += " -> "
            runner_node = runner_node.next

        return result

    def __len__(self) -> int:
        cnt: int = 0
        runner: Node = self.head

        while runner is not None:
            cnt += 1
            runner = runner.next

        return cnt

    def count_node(self) -> int:
        return self.count_node_recursive(self.head)

    def count_node_recursive(self, node) -> int:
        if node is None:
            return 0

        return 1 + self.count_node_recursive(node.next)

    def find_node(self, value) -> bool:
        runner: Node = self.head

        while runner is not None:
            if runner.value == value:
                return True

            runner = runner.next

        return False

    def delete_node(self, target_value):
        if self.head is None:
            return False

        if self.head.value == target_value:
            self.head = self.head.next
            return True
        else:
            previous: Node = self.head
            runner: Node = self.head.next

            while runner is not None:
                if runner.value == target_value:
                    previous.next = runner.next
                    return True
                previous = runner
                runner = runner.next

        return False
