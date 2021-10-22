from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        w = self. r
        prev = self.nil
        while w != self.nil:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        if u == self.nil:
            raise IndexError
        if p == self.nil:
            self.r = u
        else:
            if u.x < p.x and p.left == self.nil:
                p.left = u
            if u.x > p.x and p.right == self.nil:
                p.right = u
            if u.x == p.x:
                return False
            u.parent = p
        self.n += 1
        return True



    def find_eq(self, x : object) -> object:
        u = self.r
        while u != self.nil:
            if x < u.x:
                u = u.left
            elif x > u.x:
                u = u.right
            else:
                return u# change from return u.v to u
        return None
    
    def find(self, x: object) -> object:
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        if z == self.nil:
            return None
        return z.v
        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)
    
    def splice(self, u: BinaryTree.Node):
        if u.left != self.nil and u.right != self.nil:
            raise IndexError
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node):
        if u == None:
            return False
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left != self.nil:
                w = w.left
            u.x = w.x
            u.v = w.v
            self.splice(w)

    def remove(self, x : object) -> bool:
        w = self.find_eq(x)
        self.remove_node(w)
        if w!= None:
            return True
        else:
            return False

        # u = self.find_last(x)
        # if u != self.nil and x == u.x:
        #     self.remove_node(u)
        #     return True
        # return False

    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)

# test = BinarySearchTree()
# print(test.remove(3))
# print(test.find(2))
# print(test.add(1,"first"))
# print(test.add(2,"second"))
# print(test.add(3,"fourth"))
# print(test.size())
# print(test.find(2.5))
# print(test.remove(3))
# print(test.size())
# print(test.find(3))
# print(test.add(3,"third"))
# print(test.add(4,"fourth"))
# print(test.add(5,"fifth"))
# print(test.size())
# print(test.find_eq(3.4))
# print(test.find(3.4))

# test = BinarySearchTree()
# test.add(13,13)
# test.add(8,8)
# test.add(17,17)
# test.add(4,4)
# test.add(11,11)
# test.add(15,15)
# test.add(18,18)
# test.add(2,2)
# test.add(6,6)
# test.add(10,10)
# test.add(12,12)
# test.add(14,14)
# test.add(16,16)
# test.add(19,19)
# test.add(20,20)
# test.add(1,1)
# test.add(3,3)
# test.add(5,5)
# test.add(7,7)
# test.add(9,9)
# l = []
# print(test.bf_traverse())

# t = BinarySearchTree()
# t.add(3,"third")
# t.add(2,"second")
# t.add(5,"fifth")
# t.add(1,"first")
# t.add(4,"fourth")
# print(t.pre_order(t.r,[]))
# print(t.in_order(t.r,[]))
# print(t.post_order(t.r,[]))
# print(t.bf_traverse())
# print(t.height())
