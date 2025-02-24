# ICE Part 2: Together
'''
Create a class called Book
    String attr for “title”
    Boolean attr for is_paperback 
    Price attr (paperbacks are 9.99, hardcover are 19.99)
'''

class Book:
    def __init__(self, title, is_paperback):
        self.title = title
        self.is_paperback = is_paperback

        if is_paperback:
            self.price = 9.99
        else:
            self.price = 19.99

    def __str__(self):
        return self.title
