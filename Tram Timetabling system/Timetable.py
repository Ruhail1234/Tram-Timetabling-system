class Timetable:
    def __init__(self, tram_name, arrival_time, max_capacity, passenger_count, stop_names=None):
        self.tram_name = tname
        self.arrival_time = Atime
        self.max_capacity = Mcapacity
        self.passenger_count = Passengers
        self.stop_names = Stops if stop_names is not None else []
        Isfull = False

    def getTramName(self):
        return tname

    def getArrivalTime(self):
        return Atime

    def setArrivalTime(self):
        new_time = input("What would be the time?")
        if new_time == Atime:
            return Atime
        else:
            Atime = new_time
            return Atime

    def getMaxCapacity(self):
        return Mcapacity

    def PassengerCount(self):
        return self.passenger_count

    def updatePassengerCount(self):
        Passengers + 1
    
    def getStopNames(self):
        Stops = []
        return Stops

    def addStop():
        newStop = input("what stop do you want to add?")

        Stops.insert(100, newStop)

        return Stops

    def removeStop(self):
        stop_remove = input("What value of stop due you want to remove (eg: stops 1 is Lidcombe and you want to remove Lidcombe then typpe 1)")
        
        Stops.pop(stop_remove)

    def isTramfull(self):
        if Passengers > 2800:
            Isfull = True
            print("Beware: Tram is full.")
        else:
            Isfull = False
            print("Tram is catchable")

    
Budgerigar = bird("Budgerigar", "blue", "can't talk")
Budgerigar.fly()