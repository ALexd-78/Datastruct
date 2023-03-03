class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class Stack:

    def __init__(self):
        self.top = None



    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed_data = self.top.data
        self.top = self.top.next_node

        return removed_data


stack = Stack()
stack.push('data1')
data = stack.pop()

print(stack.top)

print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

print(stack.top.data)

print(data)

# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# print(n2.next_node)

# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# stack.push('data3')
# print(stack.top.data)
# print(stack.top.next_node.data)
# print(stack.top.next_node.next_node.data)
# print(stack.top.next_node.next_node.next_node)
# print(stack.top.next_node.next_node.next_node.data)