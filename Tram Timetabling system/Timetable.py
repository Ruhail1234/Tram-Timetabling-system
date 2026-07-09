class Timetable:
    def __init__(self, tram_name, arrival_time, max_capacity, passenger_count, stop_names=None):
        self.tram_name = tram_name
        self.arrival_time = arrival_time
        self.max_capacity = max_capacity
        self.passenger_count = passenger_count
        self.stop_names = stop_names if stop_names is not None else []

    def getTramName(self):
        print("Tram Name: ", self.tram_name)

    def getArrivalTime(self):
        print("Arriving at: ", self.arrival_time)

    def setArrivalTime(self):
        new_time = input("What would be the time?")
        self.arrival_time = new_time

    def getMaxCapacity(self):
        print("No more than ", self.max_capacity, " Passengers")

    def PassengerCount(self):
        print(self.PassengerCount)

    def updatePassengerCount(self):
        self.passenger_count + 1
    
    def getStopNames(self):
        print("Stopping at: ", self.stop_names)

    def addStop(self):
        newStop = input("what stop do you want to add?")

        self.stop_names.append(newStop)

        print(self.stop_names)

    def removeStop(self):
        stop_remove = input("What value of stop due you want to remove")
        
        self.stop_names.pop(stop_remove)

    def isfull(self):
        if self.passenger_count > 2800:
            print("Beware: Tram is full.")
        else:
            print("Tram is not full")

    
Leppingotn = Timetable("Leppington", "5:30am", "2800", "0", ["Canvely Vale", "Cabramatta", "Warwick Farm", "Liverpool", "Casula", "Glenfield", "Edminson Park", "Leppington"])
Leppingotn.getTramName()
Leppingotn.getArrivalTime()
Leppingotn.getStopNames()
Leppingotn.getMaxCapacity()