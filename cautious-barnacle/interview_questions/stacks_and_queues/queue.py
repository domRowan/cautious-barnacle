class Item:
    def __init__(self, value, left_pointer, right_pointer):
        self.value = value
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer

    def set_left_pointer(self, item_pointer):
        self.left_pointer = item_pointer

    def set_right_pointer(self, item_pointer):
        self.right_pointer = item_pointer

class Queue:
    def __init__(self):
        self.top_item = None
        self.bottom_item = None

    def push(self, value):
        item = Item(value, None, None)

        if self.top_item is None:
            self.top_item = item
            self.bottom_item = item
        else:
            previous_bottom_item = self.bottom_item
            previous_bottom_item.set_right_pointer(item)
            item.set_left_pointer(previous_bottom_item)
            self.bottom_item = item

    def pop(self):
        if self.top_item is not None:
            previous_top_item = self.top_item
            self.top_item = previous_top_item.right_pointer
            return previous_top_item.value
        else:
            return None

def create_a_queue():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5

    queue = Queue()

    queue.push(a)
    queue.push(b)
    queue.push(c)
    queue.push(d)
    queue.push(e)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    

create_a_queue()