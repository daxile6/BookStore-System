from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        if i < 0 or i > self.n:
            return None
        if i < self.n / 2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy
            for k in range(self.n, i, -1):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError("Cant get something that is out of bound")
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        x = u.x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        if w == None:
            return IndexError
        u = self.Node(x)
        u.prev = w. prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i : int, x : np.object)  :
        if i < 0 or i > self.n:
            return IndexError
        self.add_before(self.get_node(i),x)

    def _remove(self, w : Node) :


        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w

    def remove(self, i :int) :
        if i < 0 or i > self.n or self.n == 0:
            raise IndexError

        return self._remove(self.get_node(i)).x





    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        for i in range(self.n):
            y = 0
            u = self.get_node(i)
            w = self.get_node(self.n-i-1)
            while True:
                if y < self.n / 2:
                    if u.x != w.x:
                        return False
                else:
                    return True
                u = u.next
                w = w.prev
                y += 1
        return True

        # for i in range(self.n):
        #     forward = self.get_node(i)
        #     backward = self.get_node(self.n - i -1)
        #
        #     if forward.x != backward.x:
        #         return False
        #     elif forward.x == backward.x:
        #         i += 1
        # return True


        # x = True
        # y = 0
        # u = self.dummy.next
        # w = self.dummy.prev
        # while x == True:
        #     if y < self.n / 2:
        #         if u.x != w.x:
        #             x = False
        #             return x
        #     else:
        #         return x
        #     u = u.next
        #     w = w.prev
        #     y += 1



    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

# test = DLList()
# test.add(0,4)
# test.add(0,1)
# test.add(1,3)
# test.add(1,2)
# test.add(4,5)
# # print(test.get(1))
# # print(test)
# print(test.remove(2))
# print(test.remove(3))
# print(test)
#
#
# test = DLList()
# # test.add(0,"e")
# # test.add(1,"v")
# # test.add(2,"e")
# print(test.isPalindrome())