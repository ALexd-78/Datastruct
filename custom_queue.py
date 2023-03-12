class Node:
    '''Такой же, как и для класса Stack'''
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    '''Экземпляр класса иницциализируется 2 атрибутами:
    1й хранит ссылку на начало очереди,
    2й хранит ссылку на конец очереди'''
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, data):
        '''Добавляет данные в очередь.
        Связывание данных в очереди происходит прямо в методе'''
        new_node = Node(data, next_node=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def dequeue(self):
        '''Удаляет из очереди крайний левый элемент (первый добавленный)
        и возвращает данные удаленного экземпляра класса Node'''
        if self.head is None:
            return None
        dequeue_unit = self.head
        self.head = self.head.next_node
        return dequeue_unit.data

queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

# print(queue.head.data)
# print(queue.head.next_node.data)
# print(queue.tail.data)
# print(queue.tail.next_node)

# print(queue.tail.next_node.data)