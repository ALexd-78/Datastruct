import unittest


from utils import Node, Stack


class TestNode(unittest.TestCase):
    '''Тест для класса Node'''
    def test_node_(self):
        node = Node(1, None)
        self.assertEqual(node.data, 1)
        self.assertEqual(node.next_node, None)


    def test_node_next_node(self):
        node1 = Node(1, None)
        node2 = Node(2, node1)
        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.next_node.data, 1)

class TestStack(unittest.TestCase):
    '''Тест для класса Stack'''
    def test_stack_empty(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_stack_push(self):
        '''Проверяет правильность расположения адреса объекта'''
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')


    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
# if __name__ == '__main__':
#     unittest.main()