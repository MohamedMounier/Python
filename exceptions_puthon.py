try:
    number=int(input("put your lucky number : "))
    print(f"lucky number is {number}")
    numb2
except ValueError:
    print("invalid value kindly put a number.")
    number=int(input("put your lucky number : "))
    print(f"lucky number is {number}")
    exit()
except NameError:
    print("NameErrorororo")
