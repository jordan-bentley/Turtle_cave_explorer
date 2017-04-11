# Stack.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014
# added the self.get_items and self.clear_all methods - Jordan Bentley

class Stack(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates an empty LIFO stack'''

        self.items = []

    #------------------------------------------------------------

    def push(self, item):
        
        '''post: places x on top of the stack'''

        self.items.append(item)

    #------------------------------------------------------------

    def pop(self):

        '''post: removes and returns the top element of 
        the stack'''

        return self.items.pop()

    #------------------------------------------------------------

    def top(self):

        '''post: returns the top element of the stack without 
        removing it'''

        return self.items[-1]

    #------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)

    #------------------------------------------------------------

    def get_items(self):
        '''post: returns the items currently in the stack'''
        return self.items

    #-----------------------------------------------------------

    def clear_all(self):
        '''post: removes all items currently in the stack'''
        self.items = []
