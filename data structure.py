class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    #retrieves current node?
    def getData(self):
        return self.data
    #moves to next node?
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        #creating instance temp from class Node with the item I am adding
        temp = Node(item)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count


def main():

    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)

    print(mylist.size())
    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(31))



    print
    print '*******************************************************************************'
    print



    mylist2 = OrderedList()
    mylist2.add(31)

    print(mylist2.size())
    print(mylist2.search(31))
    print(mylist2.search(43))

if __name__ == '__main__':
    main()
