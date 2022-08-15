import sys
# adding LinkedList to the system path
sys.path.insert(0, '../Linked List')

from singly_linked_list import LinkedList

#Follows Last-In-Fist-Out Principle
class Stack:
    def __init__(self):
        self.__items = LinkedList()
    

    def size(self):
        return self.__items.get_size()
    

    def is_empty(self):
        return self.size() == 0


    def push(self, data):
        self.__items.add(data)
    

    def pop(self):
        if(self.is_empty()):
            return -1
        return self.__items.remove(self.size()-1) #removing the last element from the linked list
    '''
    Traversal on a stack implemented using a singly linked list is a bit completed
    Since Singly Linked List can't be traversed backwards, we have to use a temporary data structure to store the results
    Here, I have used a list as a temporary variable
    This problem will not occur when we implement stack using doubly linked list
    '''
    def display(self):
        if(self.is_empty()):
            print('Stack is empty')
            return
        temp = self.__items.get_head()
        temp_list = []
        while(temp != None):
            temp_list.append(temp.get_data())
            temp = temp.get_next()
        for item in temp_list[::-1]:
            print(item)


my_stack = Stack()
my_stack.display()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print('After Push')
my_stack.display()
my_stack.pop()
my_stack.pop()
print('After Pop')
my_stack.display()
