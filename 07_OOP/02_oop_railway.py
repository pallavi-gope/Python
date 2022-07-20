class ReservationForm:
    formType = "Railway Form"

    def printData(self):
        print(f"Name is : {self.name}\nTrain is : {self.train}")

myApplication = ReservationForm()
myApplication.name = "Arif"
myApplication.train = "Rajdhani Express"

myApplication.printData()
