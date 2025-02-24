from node import Node
from linkedlist import LinkedList
from book import Book


def main():

    # ICE  part 1: #1
    '''
    1. Create a function called to_list() that returns a list of all
    of the data attributes from each object 
    '''
    ll = LinkedList()
    ll.add_to_front("D")
    ll.add_to_front("C")
    ll.add_to_front("B")
    ll.add_to_front("A")
    lstrings = ll.to_list()
    print("\nICE 1.1:\nlist of data attributes:\n", lstrings)

    # ICE  part 1: #2
    '''
    2. Create a function called find_first_index() that returns the
    index of the lowest occurrence of a target value
    '''
    ll = LinkedList()
    ll.add_to_front("D")
    ll.add_to_front("C")
    ll.add_to_front("B")
    ll.add_to_front("A")
    ll.add_to_front("B")
    ll.add_to_front("A")
    first = ll.find_first_index("B")
    print("\nICE 1.2:\nindex of lowest occurence of target:\n", first)
    


    # ICE  part 2: Together
    '''
    In a Driver file
        Create 10 objects of book
        Create a linked chain of these 10 objects
    '''
    
    ll = LinkedList()
    ll.add_to_front(Book("Book of J", False))
    ll.add_to_front(Book("Book of I", True))
    ll.add_to_front(Book("Book of H", False))
    ll.add_to_front(Book("Book of G", True))
    ll.add_to_front(Book("Book of F", False))
    ll.add_to_front(Book("Book of E", True))
    ll.add_to_front(Book("Book of D", False))
    ll.add_to_front(Book("Book of C", True))
    ll.add_to_front(Book("Book of B", False))
    ll.add_to_front(Book("Book of A", True))

    # ICE Part 2
    '''
    Create a calculate_price_paperback in Node:
        Use recursive count as a basic example here.
    Then, make a new method in Node using this function definition
        and implement
    Try running your code in the driver
    '''
    print("\nICE 2:\nall books total price:\n", ll.calc_price())
    print("\ncount:\n",ll.count())
    print("\nlinked list of all books:\n", ll)

    # ICE Part 3: Iterative Filter
    '''
    Create a function called filter that takes in a lambda
        You can assume the lambda will expect 1 Node parameter and
        return either True or False. 
    Using a while loop, filter out all of the nodes where the lambda
        function returns False.
    '''
    paperback = lambda node: True if node.data.is_paperback else False
    new_ll = ll.iterative_filter(paperback)
    print("\nICE 3:\npaperbacks only price:\n",new_ll.calc_price())
    print("\ncount:\n", new_ll.count())
    print("\nlinked list of paperbacks only:\n",new_ll)

    # ICE Part 4: More time getting used to linked chains
    '''
    '''
    print("\nICE 4:\nsorry, can't commit time to this, skipping this part\n")
    
main()
