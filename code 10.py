class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def Insert(self,value):
        self.root = self.__Insert(self.root,value)

    def __Insert(self,root,value):
        if root is None:
            root = Node(value)
        else:
            if value < root.value:
                root.left = self.__Insert(root.left,value)
            else:
                root.right = self.__Insert(root.right,value)

        return root

    def Inorder(self):
        return self.__Inorder(self.root)

    def __Inorder(self,root):
        if root:
            self.__Inorder(root.left)
            print(root.value)
            self.__Inorder(root.right)

    def Preorder(self):
        return self.__Preorder(self.root)

    def __Preorder(self,root):
        if root:
            print(root.value)
            self.__Preorder(root.left)
            self.__Preorder(root.right)

    def Postorder(self):
        return self.__Postorder(self.root)

    def __Postorder(self, root):
        if root:
            self.__Postorder(root.left)
            self.__Postorder(root.right)
            print(root.value)

    def Height(self):
        return self.__Height(self.root)

    def __Height(self,root):
        if root is None:
            return 0
        else:
            lHeight = self.__Height(root.left)
            rHeight = self.__Height(root.right)
            if lHeight > rHeight:
                return lHeight+1
            else:
                return rHeight+1

    def Findmin(self):
        x = self.__Findmin(self.root)
        print(x.value)

    def __Findmin(self,root):
        while root is not None:
            if root.left is None:
                break
            root = root.left
        return root

    def Findmax(self):
        x = self.__Findmax(self.root)
        print(x.value)

    def __Findmax(self,root):
        while root is not None:
            if root.right is None:
                break
            root = root.right
        return root

    def Successor(self):
        a = self.__Successor(self.root)
        return a.value

    def __Successor(self,root):
        return self.__Findmin(root.right)

    def Predeccessor(self):
        a = self.__Predeccessor(self.root)
        return a.value

    def __Predeccessor(self,root):
        return self.__Findmin(root.left)

    def Delete(self,value):
        return self.__Delete(self.root,value)

    def __Delete(self,root,value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.__Delete(root.left,value)

        elif value > root.value:
            root.right = self.__Delete(root.right,value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__Findmin(root.right)
            root.value = temp.value
            root.right = self.__Delete(root.right,temp.value)
        return root



ob = BST()
ob.Insert(5)
ob.Insert(50)
ob.Insert(40)
ob.Insert(70)
ob.Insert(100)
ob.Insert(110)
print("---------Inorder-----------")
ob.Inorder()
print("---------Preorder-----------")
ob.Preorder()
print("---------Postorder-----------")
ob.Postorder()
print("---------Height-----------")
print(ob.Height())
print("---------Minimum-----------")
ob.Findmin()
print("---------Maximum-----------")
ob.Findmax()
print("---------Successor-----------")
print(ob.Successor())
print("---------Predeccessor-----------")
#print(ob.Predeccessor())
ob.Delete(40)
ob.Delete(100)
print("---------Inorder-----------")
ob.Inorder()