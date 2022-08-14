class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


    def get_data(self):
        return self.__data


    def get_next(self):
        return self.__next


    def set_data(self, data):
        self.__data = data


    def set_next(self, next_node):
        self.__next = next_node


    def get_prev(self):
        return self.__prev


    def set_prev(self, prev_node):
        self.__prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def get_head(self):
        return self.__head


    def get_tail(self):
        return self.__tail


    def set_head(self, node):
        self.__head = node


    def set_tail(self, node):
        self.__tail = node


    def get_size(self):
        return self.__size


    def clear(self):
        temp = self.__head
        while(temp!=None):
            temp1 = temp.get_next()
            temp.set_data(None)
            temp.set_next(None)
            temp.set_prev(None)
            temp = temp1
        self.__head = None
        self.__tail = None
        self.__size = 0


    def is_empty(self):
        return self.__size == 0


    def __add_first(self, data):
        new_node = Node(data)
        if(self.is_empty()):#If Linked List is empty
            self.__head = self.__tail = new_node
        else:
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
            self.__head = new_node
        self.__size += 1


    def __add_last(self, data):
        new_node = Node(data)
        if(self.is_empty()):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            new_node.set_prev(self.__tail)
            self.__tail = new_node
        self.__size += 1


    def add(self, data):
        self.__add_last(data)


    def __remove_first(self): #Deletes the first node and returns the data in it. Returns None if Linked list is already empty
        node = None #Node to be deleted
        if(self.is_empty()):
            print('Linked List Empty!')
            return
        else:
            node = self.__head
            self.__head = self.__head.get_next()
            if(self.__head == None):#If Linked List becomes empty after removing this element
                self.__tail = None
            else:
                self.__head.set_prev(None)
            self.__size -= 1
            return node.get_data()


    def __remove_last(self):
        if(self.is_empty()):
            print('Linked List Empty!')
            return
        else:
            data = self.__tail.get_data()
            self.__tail = self.__tail.get_prev()
            if(self.__tail == None):#If Linked List becomes empty after removing this element
                self.__head = None
            else:
                self.__tail.set_next(None)
            self.__size -= 1
            return data


    def insert(self, data, index): #inserts the data at a certain index position. This method returns None
        if(index<0 or index>self.__size):
            print('Invalid Index')
        elif(index==0): #Insertion at the beginning
            self.__add_first(data)
        elif(index==self.__size): #Insertion at the end
            self.__add_last(data)
        else: #Insertion in the middle
            new_node = Node(data)
            temp = self.__head 
            for i in range(0, index):
                temp = temp.get_next()
            new_node.set_next(temp)
            new_node.set_prev(temp.get_prev())
            temp.get_prev().set_next(new_node)
            temp.set_prev(new_node)
            self.__size += 1


    def remove(self, index):
        if(index<0 or index>=self.__size):
            print('Invalid index')
        elif(self.is_empty()):
            print('Linked List Empty')
        elif(index==0):
            return self.__remove_first()
        elif(index==self.__size-1):
            return self.__remove_last()
        else:
            temp = self.__head
            for i in range(0, index):
                temp = temp.get_next()
            data = temp.get_data()
            temp.get_prev().set_next(temp.get_next())
            temp.get_next().set_prev(temp.get_prev())
            '''
            The next three lines of the code are for making the data and the next part of the node to be removed as None.
            This is not needed in Python since the temp node will not have any reference once this  function is completed.
            Since temp is a local variable and the scope of temp is only within the function
            In Python, The object which does not have any reference is automatically eligible for garbage collection
            '''
            temp.set_data(None)
            temp.set_next(None)
            temp.set_prev(None)
            return data

    def displayForward(self):
        if(self.__size==0):
            print('Linked List is empty')
            return
        temp = self.__head
        while(temp != None):
            print(temp.get_data())
            temp = temp.get_next()


    def displayReverse(self):
        if(self.__size==0):
            print('Linked List is empty')
            return
        temp = self.__tail
        while(temp != None):
            print(temp.get_data())
            temp = temp.get_prev()


my_linked_list = DoublyLinkedList()
my_linked_list.add(1)
my_linked_list.add(2)
my_linked_list.add(3)
print('Diplaying Elements Forward')
my_linked_list.displayForward()
print('Diplaying Elements In Reverse')
my_linked_list.displayReverse()
my_linked_list.insert(4, 0)
print('===After Inserting===')
print('Diplaying Elements Forward')
my_linked_list.displayForward()
print('Diplaying Elements In Reverse')
my_linked_list.displayReverse()
my_linked_list.insert(5, 0)
print('===After Inserting===')
print('Diplaying Elements Forward')
my_linked_list.displayForward()
print('Diplaying Elements In Reverse')
my_linked_list.displayReverse()
my_linked_list.remove(2)
print('===After Removal===')
print('Diplaying Elements Forward')
my_linked_list.displayForward()
print('Diplaying Elements In Reverse')
my_linked_list.displayReverse()
