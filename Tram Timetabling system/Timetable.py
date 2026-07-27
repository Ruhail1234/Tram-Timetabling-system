print("============================================================")
print("          🚊 SYDNEY TRAMS TIMETABLE SYSTEM 🚊          ")
print("============================================================")
print("                 System Initialised...                      \n")

class Timetable_Model:
    def __init__(self, tram_name, arrival_time, max_capacity, passenger_count, stop_id, stop_names):
        self.tram_name = tram_name
        self.arrival_time = arrival_time
        self.max_capacity = max_capacity
        self.passenger_count = passenger_count
        self.stop_names = stop_names
        self.stop_id = stop_id

    def getTramName(self):
        print("Tram Name: ", self.tram_name)

    def getArrivalTime(self):
        print("Arriving at: ", self.arrival_time)

    def setArrivalTime(self):
        new_time = input("What would be the time? ")
        self.arrival_time = new_time

    def getMaxCapacity(self):
        print("No more than ", self.max_capacity, " Passengers")

    def PassengerCount(self):
        print(self.passenger_count)

    def updatePassengerCount(self):
        self.passenger_count += 1
    
    def getStopNames(self):
        print("Stopping at: ", self.stop_names)

    def addStop(self):
        newStop = input("what stop do you want to add? ")
        self.stop_names.append(newStop)
        print(self.stop_names)

    def removeStop(self):
        stop_remove = input("What value of stop do you want to remove? ")
        if stop_remove in self.stop_names:
            self.stop_names.remove(stop_remove)
        else:
            print("Stop not found")

    def isfull(self):
        if self.passenger_count >= self.max_capacity:
            print("Tram is full")
        else:
            print("All aboard!")

    def getStopDetails(self):
        if self.stop_id == 7123:
            self.stop_names = ["Canley Vale", "Cabramatta", "Warwick Farm", "Liverpool", "Casula", "Glenfield", "Edminson Park", "Leppington"]
        
        elif self.stop_id == 7144:
            self.stop_names = ["Bankstown", "Meryion", "Quackers hill", "Scofield", "Harbour Town"]
        

Leppington = Timetable_Model("Leppington", "5:30am", 2800, 0, 7123, [])
Leppington.getTramName()
Leppington.getStopDetails()
Leppington.getStopNames()
Leppington.removeStop()
Leppington.getStopNames()
Leppington.getArrivalTime()
Leppington.getMaxCapacity()
Leppington.isfull()

print("\n------------------------------------------------------------\n")

Harbour_Town = Timetable_Model("Harbour Town", "5:37am", 2800, 0, 7144, [])
Harbour_Town.getTramName()
Harbour_Town.getStopDetails()
Harbour_Town.getStopNames()
Harbour_Town.removeStop()
Harbour_Town.getStopNames()
Harbour_Town.getArrivalTime()
Harbour_Town.getMaxCapacity()
Harbour_Town.isfull()

