class employee():
    def __init__(self, role,position, age,gender,name) :
        self.name = name
        self.gender = gender
        self.age = age
        self.role = role
        self.position = position

    def showDetails(self):
        print("Name :"+ self.name)
        print("Gender : " + self.gender)
        print("Age : "+ str(self.age))
        print("Role : " + self.role)
        print("Position : " + self.position)
    def UpdateDetails(self):
        Name = input("What is your name: ")
        Gender = input("What is your gender: ")
        Age = input("What is your current age: ")
        Role = input("What is your current role: ")
        Position = input("What is your current position: ")
        self.name = Name
        self.gender = Gender
        self.age = Age
        self.role = Role
        self.position = Position 
s1 = employee("name","Gender","age","role","position")
s1.UpdateDetails()
s1.showDetails()


