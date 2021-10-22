import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        # todo
        open_list = ["("] #tells the code to look for open parenthesis
        close_list = [")"] #tells the code to look for open parenthesis
        stack = ArrayStack.ArrayStack() #Calls the class array stack and its function
        for i in s:
            if i in open_list:
                stack.push(i) #push into an array if there is an open parenthesis
            elif i in close_list:
                pos = close_list.index(i) #position of the closed parenthesis in the string
                if stack.size() > 0:
                    stack.pop() #if the stack is greater than zero pop the open & closed parenthesis
                else:
                    return False #if theres a close parenthesis when the size of the stack is less than zero, give false
        return stack.size() == 0

    def build_parse_tree(self, exp : str) ->str:
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node('')
        u = t.r
        i = 0
        while len(exp) != i:
            if exp[i] == '(':
                u.insert_left()
                u = u.left
            elif exp[i] in ["+", "-", "*", "/"]:
                u.x = exp[i]
                u.insert_right()
                u = u.right
            elif exp[i] == ")":
                u = u.parent
            else:
                u.x = exp[i]
                u = u.parent
            i+=1
        return t

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        left = root.left
        right = root.right
        if left != None and right != None:
            fn = op[root.x]
            return fn(self._evaluate(left), self._evaluate(right))
        elif left is None and right is None:
            t = self.dict.find(root.x)
            if t != None:
                return t
            return root.x
        else:
            if left is not None:
                return self._evaluate(left)
            else:
                return self._evaluate(right)

    def evaluate(self, exp):
        if self.dict.size() == 0:
            return 0
        # elif exp == None:
        #     None
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        
# c = Calculator()
# exp = '((a*b)+(c+d))'
# c.set_variable('a','1.3')
# c.set_variable('b','2.1')
# c.set_variable('c','2.2')
# c.set_variable('d','3')
# print(exp)
# print(c.evaluate(exp))
