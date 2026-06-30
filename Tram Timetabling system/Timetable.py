class Timetable:
    def __init__(self, btype, colour, talk):
        self.birdtype = btype
        self.birdcolour = colour
        self.birdtalk = talk

    def fly(self):
        print("The " + self.birdtype + " is flying.")

    def eat(self):
        print("The " + self.birdtype + " is eating.")
    
    def sleep(self):
        print("The " + self.birdtype + " is sleeping.")
    
    def poo(self):
        print("The " + self.birdtype + " is pooping.")
    
    def talking(self):
        if self.birdtalk == "can talk":
            dialogue = input("What do you want to teach the bird to speak")
            print(self.birdtype + " says " + dialogue)
        elif self.birdtalk == "can't talk":
            print(self.birdtype + " can't talk")

Budgerigar = bird("Budgerigar", "blue", "can't talk")
Budgerigar.fly()
Budgerigar.eat()
Budgerigar.sleep()
Budgerigar.poo()
Budgerigar.talking()

Kookaburra = bird("Kookaburra", "Brown and white", "can't talk")
Kookaburra.fly()
Kookaburra.eat()
Kookaburra.sleep()
Kookaburra.poo()
Kookaburra.talking()

Parrot = bird("Parrot", "Red and Blue", "can talk")
Parrot.fly()
Parrot.eat()
Parrot.sleep()
Parrot.poo()
Parrot.talking()