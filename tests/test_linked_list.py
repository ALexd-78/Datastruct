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

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        self.assertEqual(ll.tail.next_node, None)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.head.data, {'id': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 3})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)


    def test_print_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.print_ll(), None)


    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}])


    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})


    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_at_end('idusername')
        self.assertEqual(ll.get_data_by_id(2), 'Словарь с id=2 отсутствует')


