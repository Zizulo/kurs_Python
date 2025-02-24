
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by zero")
except ValueError:
    print("Enter only numbers please")
except TypeError:
    print("Doesnt support this type")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")

