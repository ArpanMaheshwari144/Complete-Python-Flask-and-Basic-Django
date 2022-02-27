class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @property # -> ab ye function nhi raha ab ye attribute ban gya hai
    def email(self):
        if self.fname == None:
            return "Email is not set"
        else:
            return self.fname + '.' + self.lname + "@gmail.com"

    @email.setter
    def email(self,given_email):
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]
        
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


if __name__ == '__main__':
    arpan = Employee("Arpan", "Maheshwari", 440000)
    adarsh = Employee("Adarsh","Pandey",450000)
    print(arpan.email)
    print(adarsh.email)
    adarsh.lname = "Bua"
    print(adarsh.email)
    adarsh.email = "Adarsh.kibua@gmail.com"
    print(adarsh.email)
    del adarsh.email
    print(adarsh.email)





