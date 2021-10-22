from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
        

    def add(self, x :np.object) :
        u = self.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True


    def remove(self) -> np.object:
        if self.n == 0:
            raise IndexError
        x = self.head.x
        self.head = self.head.next
        self.n-= 1
        if self.n == 0:
            self.tail = None
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

    def reverse(self):
        if self.n > 1:
            u = self.head
            v = u.next
            while v != None:
                w = v.next
                v.next = u
                u = v
                v = w
            self.head, self.tail = self.tail, self.head
            self.tail.next = None

# test = SLLQueue()
# test.add(1)
# test.add(2)
# test.add(3)
# test.add(4)
# test.add(5)
# print(test)
# test.reverse()
# print(test)
# print(test.remove())
# print(test.remove())
# print(test.remove())
# print(test.remove())
# print(test.remove())

