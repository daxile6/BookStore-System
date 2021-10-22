import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack). lololo
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b


    def get(self, i : int) -> np.object:
        if i<0 or i>=self.n :
            raise IndexError("The index of I cannot be less than 0 or greater than the number of elements in the array")
        return self.a[i]
    
    def set(self, i : int, x : np.object) -> object:
        if i<0 or i>=self.n:
            raise IndexError("cannot set a value to an index that is smaller than index of 0 or greater than the number of elements in the array")
        y = self.a[i]
        self.a[i] = x
        return y

    
    def add(self, i: int, x : np.object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if i<0 or i>self.n:
            raise IndexError("Cannot add an item at an index that is smaller than index of 0 or greater than number of elements in the array")
        if self.n == len(self.a): #
            self.resize()
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]


        #self.a[i + 1:self.n] = self.a[i:self.n - 1]
        self.a[i] = x  #sets the value of
        self.n += 1  #increments the number of elements by 1





    def remove(self, i : int) -> np.object :
        '''
            remove element i and shift all j > i one 
            position to the left
        '''
        if i < 0 or i >= self.n:
            raise IndexError("Cannot remove something that doesnt exist")

        x = self.a[i]
        for j in range(i,self.n-1):
            self.a[j] = self.a[j+1]
        #self.a[i:self.n - 2] = self.a[i + 1:self.n - 1]
        self.n -= 1
        if len(self.a) >= (3 * self.n):
            self.resize()
        return x


    def push(self, x : np.object) :
        self.add(self.n, x)
    
    def pop(self) -> np.object :
        return self.remove(self.n-1)

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x


# stack = ArrayStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
#
# while stack.size() > 0:
#     print(stack.pop())









