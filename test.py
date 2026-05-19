"""Docstring this is a simple program to see is a person can vote in NZ or not
By SRCoder on 27-8-23"""

is_resident = False
# ask the users name
name = input("What is your name?\n")
while True:
    try:
        # aks the user their age
        age = int(input("How old are you?\n"))
        break
    except:
        print
        ("That is not a number\n")
# end of while loop

# aske if they are a resident
while True:
    resident = input("Are you a resident? Y/N\n")
    if resident.lower() == "y":
        is_resident = True
        break
    elif resident.lower() == "n":
        is_resident = False
        break
    else:
        print("please type in either Y or N")
# evaluate if the person can vote
if age > 17 and is_resident:
    print("You can vote\n")
else:
    print("You can not vote\n")
