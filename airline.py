# -----------------------------------------------------------
# A simple airline ticket reservation program using Python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

# Class representing linked list node
class Node: 
    
    def __init__(self, name,flight): 
        self.name = name
        self.flight = flight
        self.next = None

# Class representing queue 

# In the queue, "front" stores the front node of linked list
# The "rear" stores the last node of linked list 
class Queue: 
    
    def __init__(self): 
        self.front = self.rear = None

    def isEmpty(self): 
        return self.front == None

    #Display passengers
    def Display(self):
        if self.front != None:
            temp = self.front
            while temp is not None:
                print(temp.name+" - "+temp.flight)
                temp = temp.next
        else:
            print("No passengers \n")
        

    #Check ticket
    def CheckTicket(self,name,flight):
        flag =0
        if self.front != None:
            temp = self.front
            while temp is not None:
                if temp.name == name and temp.flight == flight:
                    flag =1
                    print(flight+" ticket reserved for "+name+"\n")
                temp = temp.next
            if flag ==0:
                print("No "+flight+" ticket reserved for "+name+" \n")
        else:
            print("No "+flight+" ticket reserved for "+name+" \n")
            
    #Sorts the queue based on names
    def Sort(self):
        node = self.rear
        temp = self.front

        if temp.name > node.name:
            temp_node = self.front
            
            while temp_node.next is not node:
                temp_node = temp_node.next

            temp_node.next = None
            self.rear = temp_node
            self.front = node
            node.next = temp
        else:
            while temp is not None:
                if temp.name > node.name:
                    if temp.next == node:
                        self.rear = temp
                        temp.next = None
                        node.next = temp
                        prev.next = node
                        break

                    temp_node = self.front
                    while temp_node.next is not node:
                        temp_node = temp_node.next

                    temp_node.next = None
                    self.rear = temp_node
                    
                    node.next = temp
                    prev.next = node
                    break
                prev = temp
                temp = temp.next
            
        
    
    # Adds a passenger to the rear of queue 
    def EnQueue(self, name, flight): 
        temp = Node(name, flight) 
        
        if self.rear == None: 
            self.front = self.rear = temp 
            return
            
        self.rear.next = temp 
        self.rear = temp

    # Removes a passenger from the queue
    def Remove(self,name,flight): 
        
            if self.isEmpty(): 
                return
            
            temp = self.front
                
            if temp.name == name and temp.flight == flight:
                self.front = temp.next
                temp.next = None
            else:
                while temp is not None:
                    if temp.name == name and temp.flight == flight:
                        if temp.next == None:
                            self.rear = prev
                        prev.next = temp.next
                        temp.next = None
                        break

                    prev = temp
                    temp = temp.next

            if(self.front == None):
                self.rear = None

# Execution starts from here.
if __name__== '__main__':

    q = Queue()
    print("Simple flight booking")
    print("1. Reserve a ticket")
    print("2. Cancel a reservation")
    print("3. Display passengers")
    print("4. Check Ticket")
    print("5. Exit")

    while True:
        value = input("Please enter your choice:\n")
        choice = int(value)

        if choice == 1:
            name = input("Please enter your name:\n")
            flight = input("Please enter your flight:\n")
            q.EnQueue(name,flight)
            q.Sort()                                        #Sorts the queue after Enqueue.
        if choice == 2:
            name = input("Please enter your name:\n")
            flight = input("Please enter your flight:\n")
            q.Remove(name,flight)
        if choice ==3:
            q.Display()
        if choice ==4:
            name = input("Please enter your name:\n")
            flight = input("Please enter your flight:\n")
            q.CheckTicket(name,flight)
        if choice ==5:
            break
