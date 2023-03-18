import unittest

from linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
        '''Тест для класса LinkedList'''

        def test_queue_empty(self):
            ll = LinkedList()
            self.assertEqual(ll.head, None)
            self.assertEqual(ll.tail, None)


