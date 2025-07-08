age= int(input("enter your age"))

if age>=5 and age<=10:
    print("allowed to drink juice but not an energy drink")
elif age>=11 and age<=17:
    print("allowed to drink energy drink but not wine")
elif age>=18 and age<=25:
    print("allowed to drink wine without VIP")
elif age>=25 and age<=100:
    print("allowed drinks with VIP")
else:
    print("invalid age")
    pass
