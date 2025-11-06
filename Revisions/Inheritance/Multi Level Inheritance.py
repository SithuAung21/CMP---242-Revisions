class GrandFather:
    def soilder1(self):
        print("My name is Auther I and I fought in World War 1.")

class Father(GrandFather):
    def soilder2(self):
        print("My name is Auther II and fought in World War 2.")

class Child(Father):
    def soilder3(self):
        print("My name is Auther III and currently serve in Military.")

c=Child()
c.soilder1()
c.soilder2()
c.soilder3()