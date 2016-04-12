name=input("Enter name")
choice=input("(H)ello \n(G)oodbye \n(Q)uit \n \n >>>")
choice=choice.upper()
while choice!="Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Choice")
    choice=input("(H)ello \n(G)oodbye \n(Q)uit \n \n >>>")
    choice=choice.upper()
print("Finished")