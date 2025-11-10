class IceCream:
    def __init__(self, flavour):
        self.flavour = flavour
        self.price = 0

    def get_price(self):
        return self.price


class Chocolate(IceCream):
    def get_price(self):
        self.price = 3
        return self.price


class Milk(IceCream):
    def get_price(self):
        self.price = 2
        return self.price


class Vanilla(IceCream):
    def get_price(self):
        self.price = 2.8
        return self.price


class Strawberry(IceCream):
    def get_price(self):
        self.price = 2.5
        return self.price


class Mint(IceCream):
    def get_price(self):
        self.price = 3.5
        return self.price


class Order:
    def __init__(self):
        self.icecream= None

    def order(self):
        print("\nThe Following flavours are available. ")
        print("1. Chocolate ($3) ")
        print("2. Milk ($2) ")
        print("3. Vanilla ($2.8) ")
        print("4. Strawberry ($2.5) ")
        print("5. Mint ($3.5) \n")

        try:
            choice=int(input("\nChoose the Flavour: "))

            if choice == 1:
                self.icecream = Chocolate("Chocolate")
            elif choice ==2:
                self.icecream = Milk("Milk")
            elif choice == 3:
                self.icecream = Vanilla("Vanilla")
            elif choice == 4:
                self.icecream = Strawberry("Strawberry")
            else:
                self.icecream = Mint("Mint")

        except ValueError:
            print("Invalid number and try again.")

        print("\nFlavour : ", self.icecream.flavour)
        num=int(input("\nHow Many do you want: "))

        total= self.icecream.get_price()

        print("Total: ",total*num)


user1=Order()
user1.order()


