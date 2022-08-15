class Stack:
    def __init__(self):
        self.__items = []
    

    def size(self):
        return len(self.__items)
    

    def is_empty(self):
        return self.size() == 0


    def push(self, data):
        self.__items.append(data)
    

    def pop(self):
        if(self.is_empty()):
            return -1
        return self.__items.pop()
    

    def display(self):
        for item in self.__items[::-1]:
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
