class Father:
    def eyes(self):
        print("Has blue eyes")


class Mother:
    def hair(self):
        print("Has blonde hair")

class Child(Father,Mother):
    def born(self):
        print("I get those from my parents")


c=Child()
c.born()
c.hair()
c.eyes()