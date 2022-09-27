class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None 
        self.right_child = None 

class Binary_search_tree:
    def __init__(self):
        self.root = None
        self.min = 0

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def s_insert(self, value,_k):
        if self.root == None:
            self.root = Node(value)
        else:
            self.find_min()
            self._sinsert(value, self.root,self.min,_k)
            
    def find_min(self):
        if self.root == None:
            print("error")
        else:
            self._find_min(self.root)
            
    def _insert(self, value, cur_node):
        if(1):
            if (value < cur_node.value ):
                if cur_node.left_child == None:
                    cur_node.left_child = Node(value)
                    return 1
                else:
                    self._insert(value, cur_node.left_child)
                    return 1

            elif (value > cur_node.value and abs(value - cur_node.value) >= 3):
                if cur_node.right_child == None:
                    cur_node.right_child = Node(value)
                    
                    return 1
                else:
                    self._insert(value, cur_node.right_child)
                    return 1
                
    def _sinsert(self, value, cur_node, min_val,_k):
        if(abs(value - cur_node.value) < _k or value < min_val):
            print ("Request at time "+str(value)+" is not allowed")
            return 0
        # value == cur_node.value
        else:
            if (value < cur_node.value ):
                if cur_node.left_child == None:
                    print ("Request at time "+str(value)+" is allowed")
                    return 1
                else:
                    self._sinsert(value, cur_node.left_child, min_val,_k)
                    return 1

            elif (value > cur_node.value):
                if cur_node.right_child == None:
                    print ("Request at time "+str(value)+" is allowed")
                    return 1
                else:
                    self._sinsert(value, cur_node.right_child, min_val,_k)
                    return 1
            
    def _find_min(self, cur_node):
        while(cur_node.left_child != None):
            cur_node = cur_node.left_child
        self.min = cur_node.value
                

def fill_tree(tree, arr):
    for i in range(len(arr)): 
        tree.insert(arr[i])
    return tree

while True:
    try:
        x = input()
        arr_x = x.split(",")
        arr_x = list(map(int, arr_x))

        arr_y = arr_x[1:arr_x[0]+1]
        k = arr_x[arr_x[0]+1]
        print(k)
        arr_z = arr_x[arr_x[0]+2:]

        tree = Binary_search_tree()
        tree = fill_tree(tree, arr_y)

        for i in range(len(arr_z)):
            tree.s_insert(arr_z[i],k)
    except:
        break

