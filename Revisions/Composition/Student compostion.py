class Adresss:
    def __init__(self,city,country):
        self.city=city
        self.country=country

    def display(self):
        print(f"City: {self.city},Country:{self.country}")


class DateOfBirth:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def show_DOB(self):
        print(f"Day:  {self.day}, Month : {self.month}, Year: {self.year}")


class Student:
    def __init__(self,name,id,age,city,country,day,month,year):
        self.name=name
        self.age=age
        self.id=id
        self.address=Adresss(city,country) # Composition: Student HAS an Address
        self.dob=DateOfBirth(day,month,year)

    def show_details(self):
        print()
        print(f"Name: {self.name},Age:{self.age}")
        self.address.display()
        self.dob.show_DOB()

name = input("Enter Your name: ")
id=input("Enter your student ID: ")
age = int(input("Enter your age: "))
city = input("Enter city: ")
country = input("Enter country: ")
d=input("Enter your Birthday: ")
m=input("Enter your Birth Month: ")
y=input("Enter your Birth year: ")

st1=Student(name, id, age, city, country,d,m,y)
st1.show_details()
