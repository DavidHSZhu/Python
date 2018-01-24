class Node:
    def __init__(self,element):
         self.element=element
    def setNext(self,node):
        self.next=node
    def getNext(self):
        return self.next


class Sll:

    def  __init__(self):
         self.Head=Node("null")
         self.Tail=Node("null")
         self.length=0

    def getHead(self):
        return self.Head
    def getTail(self):
        return self.Tail
    def insertNode(self,index,node):


        if (index>self.length-1):
            print("this node will be  appended to tail")
            self.Head=node
            self.Tail=self.Head

        else:
            preNode=self.getNode(index)
            node.setNext(preNode.getNext())
            preNode.setNext(node)
        self.length+=1
    def appendNode(self,node):

        if (self.getTail().element=="null"):
           self.Head=node

           self.Tail=self.Head
           self.length=1
        else:
            self.Tail.setNext(node)
            self.Tail=node

        self.length+=1
    def getLength(self):
        return self.length
    def getNode(self,index):
         tempNode=self.getHead()

         if index<=self.length-1 :
           for i in range(0,index):
               tempNode=tempNode.getNext()
         else:
             print("Node is not in SINGLE LINK")
             tempNode=Node("null")
         return tempNode
    def deleteNode(self,index):
        if index==0:
           self.Head=self.Head.getNext()
        elif (index>self.length-1) :
            print("wrong index value")
        elif (index==self.length-1):
            self.Tail=self.getNode(index-1)
        else:
            preNode=self.getHead()

            for i in range(0,index-1):

                preNode=preNode.getNext()
            tempNode=preNode.getNext()
            preNode.setNext(tempNode.getNext())

mysll=Sll()


mysll.insertNode(0,Node("0"))
mysll.appendNode(Node("1"))
mysll.appendNode(Node("2"))
mysll.appendNode(Node("3"))
mysll.insertNode(2,Node("2.5"))
mysll.insertNode(2,Node("2.6"))

print("print all of NODES")
for i in range(0,mysll.getLength()):
    print (mysll.getNode(i).element)

print("###################################")

