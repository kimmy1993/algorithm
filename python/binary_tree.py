import time
import random
import queue

class Tree_Node(object):
    tree_data = None
    left = right = None
    
    def __init__(self):
        self.tree_data = None
        self.left = self.right = None
     
    def insert(self,Node,data):
        if Node== None:
            Node = Tree_Node()
            Node.insert(Node,data)
        elif Node.tree_data == None:
            Node.tree_data = data
        elif data < Node.tree_data:
           Node.left = self.insert(Node.left,data)
        else:
            Node.right = self.insert(Node.right,data)

        return Node

    def delete(self,Node, data):
        if not Node:
            pass
        elif Node.tree_data == data:
            if not Node.left and not Node.right:
                Node = None
            elif Node.left and not Node.right:
                Node = Node.left
            elif Node.right and not Node.left:
                Node = Node.right
            else:
                save_l = Node.left
                save_r = Node.right
                parent = Node.right
                if not parent.left:
                    parent.left = save_l
                    Node = parent
                else:
                    while parent.left.left:
                        parent = parent.left
                    Node = parnet.left
                    parent.left = Node.right
                    Node.left = save_l
                    Node.right = save_r
        elif Node.tree_data < data:
            Node.right = Node.delete(Node.right,data)
        else:
            Node.left = Node.delete(Node.left,data)

        return Node


    def search_delete(self,Node):
        if not Node.left.left:
            return Node
        else:
            return Node.search_delete(Node.left)

    def DFS(self,Node,depth):
        if not Node:
            return
        print("Depth: " + str(depth) + " data: " + str(Node.tree_data))

        if not Node.left and not Node.right:
            return
        elif Node.left and not Node.right:
            print("Left")
            Node.DFS(Node.left,depth+1)
        elif Node.right and not Node.left:
            print("Right")
            Node.DFS(Node.right,depth+1)
        else:
            print("Left")
            Node.DFS(Node.left,depth+1)
            print("Right")
            Node.DFS(Node.right,depth+1)
        return

    def BFS(self,Node):

        q = queue.Queue()
        i = 1
        q.put([Node,i,""])

        while not q.empty():
            list = q.get()
            if not list[0]:
                continue
            else:
                i = list[1]
                print(list[2])
                print("Depth: " + str(list[1]) + " data: " + str(list[0].tree_data))
                q.put([list[0].left,i+1,"Left"])
                q.put([list[0].right,i+1,"Right"])



        return


#main
tree = Tree_Node()
num = 0

list_data = []

for i in range(11):
    list_data.append(random.randrange(1,50))
    tree = tree.insert(tree,list_data[i])

print("input : " + str(list_data))
print("delete : " + str(list_data[5]))


tree = tree.delete(tree,list_data[5])
print("")
print("BFS : ")
tree.BFS(tree)

print("")
print("DFS : ")
tree.DFS(tree,1)