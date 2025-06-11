# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

T1 = TreeNode(1,
              TreeNode(3, TreeNode(4), TreeNode(5)),
              TreeNode(6, TreeNode(7), TreeNode(8)))

def isFeuille(T:TreeNode):
    if T.left == None and T.right == None :
        return True 
    return False


def taille(T:TreeNode):
    if  T == None :
        return 0
    
    return 1  + taille(T.left) + taille(T.right)

def hauteur(T:TreeNode):
    if  T == None :
        return 0
    return 1 + max( hauteur(T.left) , hauteur(T.right))


def compteurfeuille(T:TreeNode):
    if  T == None :
        return 0
    return compteurfeuille(T.left) +compteurfeuille(T.right)

def sommmevaleurs(T:TreeNode):
    if T == None:
        return 0
    return T.val + sommmevaleurs(T.left) +sommmevaleurs(T.right)


def min_valeur(T: TreeNode):
    if T is None:
        return float('+inf')  
    
    return min(T.val, min_valeur(T.left), min_valeur(T.right))

def max_valeur(T:TreeNode):
    if T is None:
        return float('-inf')  
    
    return max(T.val, max_valeur(T.left), max_valeur(T.right))

def search(T:TreeNode,n:int):
    
    if T is None :
        return False
    
    if T.val == n:
        return True 
    
    return search(T.left,n) or search(T.right,n)

