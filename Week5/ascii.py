LOWER = 10
UPPER = 100

def get_number():
    low=input("Enter a number({}-{}):".format(LOWER,UPPER)).strip()
    while not low.isdecimal():
        print("Please enter a valid number")
        low=(input("Enter a number({}-{}):".format(LOWER,UPPER)).strip())
    int1=int(low)
    while int1<LOWER or int1>UPPER:
        print("Please enter a valid number")
        low=(input("Enter a number({}-{}):".format(LOWER,UPPER)).strip())
        int1=int(low)
    upp=input("Enter a number({}-{}):".format(LOWER,UPPER)).strip()
    while not upp.isdecimal():
        print("Please enter a valid number")
        low=(input("Enter a number({}-{}):".format(LOWER,UPPER)).strip())
    int2=int(upp)
    while upp<low or upp>UPPER:
        print("Please enter a valid number")
        upp=(input("Enter a number({}-{}):".format(LOWER,UPPER)).strip())
        int2=int(upp)
    return int1,int2
low,upp=get_number()
for i in range(low,upp):
    print("{} {}".format(i, chr(i)))