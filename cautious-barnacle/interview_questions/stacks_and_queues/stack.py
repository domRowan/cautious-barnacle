
class Item:
    def __init__(self, value, leftPointer, rightPointer):
        self.value = value
        self.leftPointer = leftPointer
        self.rightPointer = rightPointer

    def setLeftPointer(self, itemPointer):
        self.leftPointer = itemPointer

    def setRightPointer(self, itemPointer):
        self.rightPointer = itemPointer


class Stack:
    def __init__(self):
        self.topItem = None

    def push(self, item):
        item = Item(item, None, None)

        if self.topItem is None:
            self.topItem = item
        else:
            previousTopItem = self.topItem
            previousTopItem.setRightPointer(item)
            item.setLeftPointer(previousTopItem)
            self.topItem = item

    def pop(self):
        if self.topItem is not None:
            previousTopItem = self.topItem
            self.topItem = self.topItem.leftPointer
            return previousTopItem.value
        else:
            return None


def create_a_stack():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5

    stack = Stack()

    stack.push(a)
    stack.push(b)
    stack.push(c)
    stack.push(d)
    stack.push(e)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    
create_a_stack()
