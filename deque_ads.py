class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("remove front from empty deque")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("remove rear from empty deque")

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek front from empty deque")

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek rear from empty deque")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
deque = Deque()
deque.add_front(1)
deque.add_rear(2)
print(deque.remove_front())  # Output: 1
print(deque.remove_rear())  # Output: 2
print(deque.is_empty())  # Output: True
