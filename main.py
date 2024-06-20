def main():
    meow(getnum())


def getnum():
    while True:
        n = int(input("Give an int: "))
        if n >= 0:
            return n

def meow(n):
    for _ in range (n):
        print ("Meow")

main()