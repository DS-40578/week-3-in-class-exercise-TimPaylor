# ICE
'''
Make a class called LinkedList
    Attr for head (set to None initially)
    Method for add_to_front together
    Method for iterative find() together
'''

from node import Node
from book import Book

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def find(self, target_value):
        current = self.head
        while current is not None:
            if current.data == target_value:
                return current
            current = current.next
        return None

    # ICE  part 1: #1
    '''
    1. Create a function called to_list() that returns a list of all
    of the data attributes from each object 
    '''
    def to_list(self):
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(str(current.data))
            current = current.next
        return data_list

    # ICE  part 1: #2
    '''
    2. Create a function called find_first_index() that returns the
    index of the lowest occurrence of a target value
    '''
    def find_first_index(self, data):
        current = self.head
        index = 0
        while current.data != data:
            index += 1
            current = current.next
        return index

    def count(self):
        return self.head.count()

    def iterative_count(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def calc_price(self):
        return self.head.calculate_price()

    # ICE Part 3: Iterative Filter
    '''
    Create a function called filter that takes in a lambda
        You can assume the lambda will expect 1 Node parameter and
        return either True or False. 
    Using a while loop, filter out all of the nodes where the lambda
        function returns False.
    '''
    def iterative_filter(self, predicate):
        current = self.head
        new_ll = LinkedList()
        while current is not None:
            if predicate(current) == True:
                new_ll.add_to_front(current.data)
            current = current.next
        return new_ll
        
    def __str__(self):
        return_str = ""
        current = self.head
        while current is not None:
            return_str += str(current) + " "
            current = current.next
        return return_str
