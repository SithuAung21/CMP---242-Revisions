try:
    x=int(input("Enter the numerator: "))
    y=int(input("Enter the denominator: "))
    z=x/y
except ZeroDivisionError:
    print("Can't be divided by Zero")
except ValueError:
    print("Please enter only number")
except Exception:
    print("Something went wrong")

finally:
    print("Please check your input type.")