class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.userLastName = last_name
        self.userFullName = first_name + " " + last_name
        

    def sayName(self):
        print(self.username)


    def sayLastName(self):
        print(self.userLastName)

    def sayFullName(self):
        print(self.userFullName)    
     



