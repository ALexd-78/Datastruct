class Node:
    '''Класс Node имеет 2 атрибута:
    данные и ссылка на следующи  узел'''
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Stack:
    '''Хранит ссылку на верхний(крайний в стэке) узел'''
    def __init__(self):
        self.top = None



    def push(self, data):
        '''Добавляет данные в стэк.
        Связывание данных в стэке происходит прямо в методе'''
        next_node = self.top
        new_node = Node(data, next_node)
        self.top = new_node

    def pop(self):
        '''Удаляет из стэка верхний (последним добавленный) элемент и
        возвращает данные удалённого экземпляра класса Node'''
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