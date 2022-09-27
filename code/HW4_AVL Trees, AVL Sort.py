class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.h = 0

class AVL_tree:
    def __init__(self):
        self.root = None

    def LR(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x
        x.parent = y
        x.h = x.h - 1 - max(0, y.h)
        y.h = y.h - 1 + min(0, x.h)
        
    def RR(self, x):
        y = x.left
        x.left = y.right;
        if y.right != None:
            y.right.parent = x
        
        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        x.h = x.h + 1 - min(0, y.h)
        y.h = y.h + 1 + max(0, x.h)
        
    def insert(self, key):
        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.check_p(node)
        
    def check_p(self, node):
        if node.h < -1 or node.h > 1:
            self.balance(node)
            return;

        if node.parent != None:
            if node == node.parent.left:
                node.parent.h -= 1

            if node == node.parent.right:
                node.parent.h += 1

            if node.parent.h != 0:
                self.check_p(node.parent)
    def balance(self, node):
        if node.h > 0:
            if node.right.h < 0:
                self.RR(node.right)
                self.LR(node)
            else:
                self.LR(node)
        elif node.h < 0:
            if node.left.h > 0:
                self.LR(node.left)
                self.RR(node)
            else:
                self.RR(node)
    def _in_order_traversal(self):
        a = []
        return self.in_order_traversal(self.root,a)
        
    def in_order_traversal(self, node, a):
        if node != None:
            self.in_order_traversal(node.left,a)
            a.append(node.data)
            self.in_order_traversal(node.right,a)
        return a

while True:
    try:
        x = input()
        arr_x = x.split(",")
        arr_x = list(map(int, arr_x))
        
        bst = AVL_tree()
        for i in arr_x:
            bst.insert(i)
        ans_arr = bst._in_order_traversal()   
        
        print("Inorder traversal: [",end = "")
        for i in range(len(ans_arr)-1):
            print(str(ans_arr[i]) + ", ",end = "")
        print(str(ans_arr[len(ans_arr)-1])+"]")
        
    except:
        break
