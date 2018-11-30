# Title: Binary Search Tree in Python
# Author: Hintea, D.
# Date: November 2018
# Availability: http://cumoodle.coventry.ac.uk located in 210CT Week 5
# Start of the Used Code

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
#-----------------------------------------------#
#This is my Function for the tree to Print in PreOrder

def preorder(tree):
    print(tree.value)
    if(tree.left!=None):
        preorder(tree.left)
    if(tree.right!=None):
        preorder(tree.right)
        
#--------------------------------------------#
def OpenPara():
    paragraph = open("ParagraphTask1.txt","r")
    para = paragraph.read().lower().split()
    freq = {}
    for i in para:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] +=1
    print(freq) 
    return para    
    
def TreeFind (tree, item,):
    if tree == None:
        print("Item not Found")
    elif tree.value == item:
        print(tree.value)
        print("Item is in Tree")
    elif item < tree.value:
        TreeFind(tree.left, item)
        print(tree.value, "Searching Left side of tree")
    else:
        TreeFind(tree.right, item)
        print(tree.value, "Searching Right side of tree")

#Task 2 Delete Node Function
        
def Node_Delete(tree, item):
    if tree == None:
        print("Node Not Found")
    elif item < tree.value:
        tree.left = Node_Delete(tree.left, item)
        
    elif item > tree.value:
        tree.right = Node_Delete(tree.right, item)
        
    elif item == tree.value:
        if tree.left == None and tree.right == None:
            print("Node without children deleted")
            return None
        if tree.left != None and tree.right == None:
            temp = tree.left
            
            return temp
        if tree.right!=None and tree.left == None:
            temp = tree.right
            
            return temp
        else:
            temp = minNode(tree.right)
            tree.value = temp.value
            tree.right = Node_Delete(tree.right, temp.value)
    return tree

def minNode(item):
    tree = item
    if tree.left != None:
        return minNode(tree.left)
    return tree

#End of Task 2 Delete Node Code 
          
lst = OpenPara()
for i in range (len(lst)):
    if i < 1:
        t = tree_insert(None,lst[i])
    else:
        tree_insert(t,lst[i])
preorder(t)
TreeFind(t, input("Enter a word to find: "))
Node_Delete(t,input("Enter a word to delete: "))
print()
preorder(t)