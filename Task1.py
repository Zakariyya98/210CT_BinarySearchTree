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
        
def tree_insert( tree, item):
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
        
#------------------------------------------------#        



#
#if __name__ == '__main__':
 #   t=tree_insert(None,6);
  #  tree_insert(t,5)
   # tree_insert(t,7)
#    tree_insert(t,1)
 #   tree_insert(t,3)
  #  tree_insert(t,4)
   # tree_insert(t,9)
  #  preorder(t)

# This is the Function to open and read the Paragraph

# This is my line split ... To be continued.




def OpenPara():
    paragraph = open("ParagraphTask1.txt","r")
    para = paragraph.read().lower().split()
    return para    
    

lst = OpenPara()

t = tree_insert(None,lst[0])
for i in range (len(lst)):
    tree_insert(t,lst[i])
preorder(t)






#OpenPara = open("ParagraphTask1.txt", "r")
#wordsfinallysplit = f.split()



    
 



