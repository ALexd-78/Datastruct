class Node:
    '''Класс Node имеет 2 атрибута:
        данные и ссылка на следующи  узел'''
    def __init__(self, data: list):
        self.data = data
        self.next_node = None


class LinkedList:
    '''Хранит ссылку на начало связанного списка и на его конец'''
    def __init__(self):
        self.head = None
        self.tail = None



    def insert_beginning(self, data: list):
        '''принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node



    def insert_at_end(self, data):
        '''принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка'''
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def print_ll(self):
        '''Выводит данные в консоль из односвязного списка'''
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


    def to_list(self):
        '''Возвращает список с данными, содержащимися в односвязном списке'''
        ll_node = []
        node = self.head
        while node:
            ll_node.append(node.data)
            node = node.next_node
        return ll_node


    def get_data_by_id(self, id):
        '''возвращает первый найденный в LinkedList словарь с ключом id, значение которого равно переданному в метод значению.'''
        node = self.head
        while node:
            try:
                if node.data['id'] == id:
                    return node.data
                    break
            except TypeError:
                print("Данные не являются словарем или в словаре нет id")
            node = node.next_node
        if node is None:
            return f'Словарь с id={id} отсутствует'





ll = LinkedList()
# ll.insert_beginning({'id': 1})
# ll.insert_at_end({'id': 2})
# ll.insert_at_end({'id': 3})
# ll.insert_beginning({'id': 0})
# print(ll.head.data)
# print(ll.head.next_node.data)
# print(ll.tail.data)
# print(ll.tail.next_node)
# lst = ll.to_list()
# print(lst)

# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
# ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll.get_data_by_id(2)
print(user_data)
