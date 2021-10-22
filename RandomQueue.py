import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
                    remove a random element
                    You can call the method of the parent class using super(). e.g.
                    super().remove()
                '''
        if self.n == 0: # if the number of elements is zero execute this if statement
            raise IndexError("No elements to remove")
        random_element = random.randint(0, self.n - 1)  #assigning a random integer
        #assigned the random integer to swap_index variable
        swap_index = random_element
        self.a[(self.j + swap_index) % len(self.a)], self.a[self.j] = \
            self.a[self.j], self.a[(self.j + swap_index) % len(self.a)] #swaps the index position, ex (a,b) = (b,a)

        x = self.a[self.j]  # removing the first element, "first in first out"
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        #checking preconditions
        if len(self.a) >= (3 * self.n):
            self.resize()
        return x

# test = RandomQueue()
# for i in range(4):test.add(i)
# print(test)
# for i in range(2):print(test.remove())
# for i in range(4):test.add(i)
# print(test)
# for i in range(6):print(test.remove())
     




