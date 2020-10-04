

class LinkedList():
    """
    Simplist linked list implementation using 2 attributes.

    Attributes
    ----------
    link : LinkedList
        link to next point in list, can be none to represent the end point
    data : str
        data represented in that point of the linked list

    Methods
    -------
    Present(search):
        searches for a value in the list
    sort():
        sorts linked list using in-built string sorting
    printAll():
        prints all values in linked list starting from current and moving deeper
    reverse():
        reverses order of linked list
    
    """

    def __init__(self,link,data):
        """
        Constructs the linked list

        Parameters
        ----------
            link : LinkedList
                link to next point in list, can be none to represent the end point
            data : str
                data represented in that point of the linked list
        """
        self.link = link
        self.data = data

    def __getitem__(self,i):
        count = 0
        current = self
        while count != i and current != None:
            current = current.link
            count +=1
        if count == i and current != None:
            return current.data
        else:
            raise IndexError(str(i) + ": is out of bounds of the list. The current list length is: "+str(count))

    def __setitem__(self,i,value):
        count = 0
        current = self
        while count != i and current != None:
            current = current.link
            count +=1
        if count == i and current != None:
            current.data = value
        else:
            raise IndexError(str(i) + ": is out of bounds of the list. The current list length is: "+str(count))    

    def __len__(self):
        count = 0
        current = self
        while current != None:
            current = current.link
            count+=1
        return count

    def present(self,search):
        """
        Searches for a value in the list

        Parameters
        ----------
        search : str
            the string to search for in the list

        Returns
        -------
        True/False (boolean): boolean based on whether string is present in list
        """
        if self.data != search:
            current = self.link
            while current != None:
                if current.data == search:
                    return True
                current = current.link
            return False
        else:
            return True

    def sort(self):
        """
        Sorts list using in-built string sorting

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        vals = [self.data]
        current = self.link
        while current != None:
            vals.append(current.data)
            current = current.link
        vals.sort()
        x = LinkedList(None,vals[0])
        for i in range(1,len(vals)):
            x = LinkedList(x,vals[i])
        self.data = x.data
        self.link = x.link
        
    def printAll(self):
        """
        Prints all data points in linked list from current to deepest point in the list

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        current = self.link
        print(self.data)
        while current != None:
            print(current.data)
            current = current.link

    def reverse(self):
        """
        Reverses the order of the linked list

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        current = LinkedList(None,self.data)
        link = self.link
        while link != None:
            current = LinkedList(current,link.data)
            link = link.link
        self.data = current.data
        self.link = current.link

        


x = LinkedList(None,"12")
x = LinkedList(x,"4")
x = LinkedList(x,"7")
x = LinkedList(x,"8")
x = LinkedList(x,"5")
x = LinkedList(x,"2")
print(x.present("7"))
x.sort()
x.printAll()
print("")
x.reverse()
x.printAll()
print("")
x[3] = 17
print(x[3])
print(len(x))
