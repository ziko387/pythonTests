from operator import truediv

print("WELCOME TO OUR ST JAMES SCHOOL ADMISSION LIST")
name= input("Enter your name kindly:")
print(f"welcome to our add list :{name}")
age=int(input("Enter your age:"))
if age >= 5 and age<=9:
    print("ENTER YOUR CLASS")
    print("1.playgroup")
    print("2. pre_1")
    print("3.pre_2")
    Class= input("enter your class kindly:")
    choice={
        "1":"playgroup",
        "2":"pre_1",
        "3":"pre_2"
    }
    get_class= choice.get(Class)
    print(f"dear {name},you have been placed in {get_class}")
elif age >=10 and age <=19:
    print("ENTER YOUR CLASS")
    print("1.GRADE1")
    print("2.GRADE2")
    print("3.GRADE3")
    print("4.GRADE4")
    print("5.GRADE5")
    print("6.GRADE6")
    print("7.GRADE7")
    print("8.GRADE8")
    print("9.GRADE9")
    grade= input("Enter your class")
    loom={
        "1":"GRADE1",
        "2":"GRADE2",
        "3":"GRADE3",
        "4":"GRADE4",
        "5":"GRADE5",
        "6":"GRADE6",
        "7":"GRADE7",
        "8":"GRADE8",
        "9":"GRADE9"
    }
    get_loom= loom.get(grade)
    print(f"dear {name},you have been placed in {get_loom}")
elif age >=20 and age >=100:
    print(f"DEAR {name} YOU CANNOT JOIN OUR INSTITUTION BECAUSE YOU HAVE EXCEEDED THE AGE REQUIRED TO JOIN OUR INSTITUTION")


else:
    print(f"DEAR {name} YOU ARE NOT ADMITTED BECAUSE YOU HAVE NOT REACHED THE REQUIRED AGE TO JOINING OUR INSTITUTION ")
