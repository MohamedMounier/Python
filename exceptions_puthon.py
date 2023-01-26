# python error types link
# https://nouvil.net/python-error-types/
try:
    number=int(input("put your lucky number : "))
    print(f"lucky number is {number}")
    #numb2
    # numb2 will throw a name error as there is no assigned value
    # value error is when there is a different type expected
except ValueError:
    print("invalid value kindly put a number.")
    number=int(input("put your lucky number : "))
    print(f"lucky number is {number}")
    exit()
except NameError:
    print("NameErrorororo")
