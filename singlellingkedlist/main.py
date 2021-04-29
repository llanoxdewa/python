# mengenai list wadidaw
# linked list

class singlyLinkedList:
    class _Node:
        def __init__(self, element, nextnode = None):
            self.element = element
            self.nextNode = nextnode
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __str__(self):
        result = ""
        pointer = self._head
        while pointer != None:
            result += str(pointer.element) + " "
            pointer = pointer.nextnode
        return result
    def add_first(self,element):
        newNode = self._Node(element)
        newNode.nextnode = self._head
        self._head = newNode
        self._size += 1
    def __len__(self):
        return self._size
        
mylist = singlyLinkedList()
mylist.add_first(10)
mylist.add_first(20)
mylist.add_first(30)
print(str(mylist))
print(len(mylist))

       