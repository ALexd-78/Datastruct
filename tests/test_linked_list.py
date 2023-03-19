import unittest

from linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    '''Тест для класса Node'''
    def test_node(self):
        node = Node(1)
        self.assertEqual(node.data, 1)
        self.assertEqual(node.next_node, None)


class TestLinkedList(unittest.TestCase):
        '''Тест для класса LinkedList'''

        def test_ll_empty(self):
            ll = LinkedList()
            self.assertEqual(ll.head, None)
            self.assertEqual(ll.tail, None)


