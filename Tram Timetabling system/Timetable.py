#Note: This a program which is under software development stage and the stop names of the trams are not accurate. Some of the methods on this will not be used on the user end such as Removestop and Addstop. Separate files will be made for the interaction of user and the interaction of staff members.

print("============================================================")
print("          🚊 SYDNEY TRAMS TIMETABLE SYSTEM 🚊          ")
print("============================================================")
print("                 System Initialised...                      \n")

#The class of timtable modellling system with the attributes such as tram name, arrival time, max capacity, etc initialised before use.
class Timetable_Model:
    def __init__(self, tram_name, arrival_time, max_capacity, passenger_count, stop_id, stop_names):
        self.tram_name = tram_name
        self.arrival_time = arrival_time
        self.max_capacity = max_capacity
        self.passenger_count = passenger_count
        self.stop_names = stop_names
        self.stop_id = stop_id

#The function that is used to print the stop names of a tram
    def getTramName(self):
        print("Tram Name: ", self.tram_name)

#The function that prints the arrival time of a Tram
    def getArrivalTime(self):
        print("Arriving at: ", self.arrival_time)

#The function that sets the arrival time for a tram
    def setArrivalTime(self):
        new_time = input("What would be the time? ")
        self.arrival_time = new_time
        if self.arrival_time == "6:00am" or "6:30am" or "7:00am" or "7:30am" or "8:00am" "3:00pm" or "3:30pm" or "4:00pm":
                    self.passenger_count = 200

#The method that is used to print the max capacity of a tram
    def getMaxCapacity(self):
        print("No more than ", self.max_capacity, " Passengers")

#This methods shows the amount of passenger tht a tram currently holds
    def PassengerCount(self):
        print("Number of Passenger: ", self.passenger_count)

#This method updates the passenger count, it will be improved in the future by adding customer with the amount of opal cards tapped on a train.
    def updatePassengerCount(self):
        self.passenger_count += 1

#Thiis method prints the stop names for a tram according to their stop id
    def getStopNames(self):
        print("Stopping at: ", self.stop_names)

#Used to add a stop to a tram.
    def addStop(self):
        newStop = input("what stop do you want to add? ")
        self.stop_names.append(newStop)
        print("Stopping at: ", self.stop_names)

#Used to remove a stop from the list of stop name of a tram
    def removeStop(self):
        stop_remove = input("What value of stop do you want to remove? ")
        if stop_remove in self.stop_names:
            self.stop_names.remove(stop_remove)
        else:
            print("Stop not found")

# A methods that checks whether a tram is full or not.
    def isfull(self):
        if self.passenger_count >= self.max_capacity:
            print("Tram is full")
        else:
            print("All aboard!")

#This methods gets the details of all the stop for a trams and assigns stops to a tram according to their stop id.
    def getStopDetails(self):
        if self.stop_id == 7123:
            self.stop_names = ["Canley Vale", "Cabramatta", "Warwick Farm", "Liverpool", "Casula", "Glenfield", "Edminson Park", "Leppington"]
        
        elif self.stop_id == 7144:
            self.stop_names = ["Bankstown", "Meryion", "Quackers hill", "Scofield", "Harbour Town"]

#This inheritance is an example of the first tram that will have its information displayed.
Leppington = Timetable_Model("Leppington", "5:30am", 400, 0, 7123, [])
Leppington.setArrivalTime()
Leppington.getTramName()
Leppington.getStopDetails()
Leppington.getStopNames()
Leppington.removeStop()
Leppington.addStop()
Leppington.updatePassengerCount()
Leppington.PassengerCount()
Leppington.getArrivalTime()
Leppington.getMaxCapacity()
Leppington.isfull()

print("\n------------------------------------------------------------\n")

#This inheritance is another tram which will have its information displayed on the timetable after it is fully printed.
Harbour_Town = Timetable_Model("Harbour Town", "5:37am", 400, 0, 7144, [])
Harbour_Town.setArrivalTime()
Harbour_Town.getTramName()
Harbour_Town.getStopDetails()
Harbour_Town.getStopNames()
Harbour_Town.removeStop()
Harbour_Town.addStop()
Harbour_Town.updatePassengerCount()
Harbour_Town.PassengerCount()
Harbour_Town.getArrivalTime()
Harbour_Town.getMaxCapacity()
Harbour_Town.isfull()