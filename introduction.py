class robot:
    name = "ANDREW"
    age = "One Month"
    founder = "SREE RANAGRAJ"
    hobbies = "Helping Others"

    def introduction(self):
        print("Hi I am Robot")

    def details(self):
        print("My name is", self.name)
        print("I am", self.age,"old")
        print("I was founded by", self.founder)
        print("My hobby is", self.hobbies)

ob = robot()
ob.introduction()
ob.details()
