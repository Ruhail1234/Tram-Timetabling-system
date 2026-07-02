class Timetable:
    def __init__(self, tram_name, arrival_time, max_capacity, passenger_count, stop_names):
        self.tram_name = tname
        self.arrival_time = Atime
        self.max_capacity = Mcapacity
        self.passenger_count = Passengers
        self.stop_names = Stops

    def getTramName(self):
        return self.tram_name

    def getArrivalTime(self):
        return self.arrival_time

    def setArrivalTime(self):
        new_time = input("What would be the time?")
        if new_time == self.arrival_time:
            return self.arrival_time
        else:
            self.arrival_time = new_time

    def getMaxCapacity(self):
        return self.max_capacity

    def PassengerCount(self):
        return self.passenger_count

    def updatePassengerCount(self):
        self.passenger_count + 1
    
    def getStopNames():
        return self.stop_names

    
    

    
Budgerigar = bird("Budgerigar", "blue", "can't talk")
Budgerigar.fly()