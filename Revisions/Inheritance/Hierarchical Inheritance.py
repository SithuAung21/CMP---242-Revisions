class EuropeanUnion:
    def EU(self):
        print("I'm the one of the members of the EU ")


class Germany(EuropeanUnion):
    def germany(self):
        print("I am Germany")

class France(EuropeanUnion):
    def france(self):
        print("I am France")


class Italy(EuropeanUnion):
    def italy(self):
        print("I am Italy")

g=Germany()
g.germany()
g.EU()

f=France()
f.france()
f.EU()

i=Italy()
i.italy()
i.EU()