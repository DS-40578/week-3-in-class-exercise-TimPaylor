# ICE
'''
Make Node as defined in these slides
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # ICE  part 2: Together
    '''
    Implement a count function
    '''
    def count(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.count()

    # ICE Part 2
    '''
    Create a calculate_price_paperback in Node:
        Use recursive count as a basic example here.
    '''
    def calculate_price(self):
        '''
        may only work with book objects
        '''
        if self.next is None:
            return self.data.price
        return self.data.price + self.next.calculate_price()

    def __str__(self):
        return str(self.data)


