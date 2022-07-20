#write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information 
#of trains running under indian railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print(f"The name of the train is : {self.name}.\nThe seats available in this train are : {self.seats}")

    def getFareInfo(self):
        print(f"The price of the ticket is : Rs. {self.fare}")

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked, your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry! the train is full")

    def cancelTicket(self):
        self.seats = self.seats + 1
        print("Your seat has been cancelled")

intercity = Train("Intercity Express : 14015", 90, 200)
print("**************************************************************")
intercity.getStatus()
intercity.getFareInfo()
intercity.bookTicket()
print("**************************************************************")
intercity.getStatus()
print("**************************************************************")
intercity.cancelTicket()
intercity.getStatus()
print("**************************************************************")
