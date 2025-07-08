age= int(input("enter your age"))


if age>=5 and age<=10:
    print("allowed to drink juice but not an energy drink")
    print("types of juice")
    print("1.fanta")
    print("2.sprite")
    print("3.delamonte")
    print("4.cocacola")
    choice= input("select your favorite juice:")
    juice={
        "1":"fanta",
        "2":"sprite",
        "3":"delamonte",
        "4":"cocacola"

    }
    select_juice= juice.get(choice)
    print(f"you have selected:{select_juice} sucessfuly")
elif age>=11 and age<=17:
    print("allowed to drink energy drink but not wine")
    print("ENERGY DRINKS")
    print("1.Monster")
    print("2.simba")
    print("2.red bull")
    Drinks= input("Enter your energy drink:")
    energy={
        "1":"Monster",
        "2":"simba",
        "3":"red bull"
    }
    get_drinks= energy.get(Drinks)
    print(f"you have selected :{get_drinks} successfully")

elif age>=18 and age<=25:
    print("allowed to drink wine without VIP")
    print("SELECT YOUR DRINKS")
    print("1.chrome")
    print("2.Tusker")
    print("3.county")
    print("4. Wala")
    print("5.Amarula")
    answer= input("enter your drinks")
    Geo={
        "1":"chrome",
        "2":"Tusker",
        "3":"county",
        "4":"Wala",
        "5":"Amarula"
    }
    gain_drink= Geo.get(answer)
    print(f"you have selected :{gain_drink} successfully")

elif age>=25 and age<=100:
    print("allowed drinks with VIP")
    print("SPECIAL VIP DRINKS")
    print("1.king walker")
    print("2.Alexa")
    print("3.jakim")
    special=input("Enter your vip drink: ")
    Great={
        "1":"king walker",
        "2":"Alexa",
        "3":"jakim"
    }
    vip_drink=Great.get(special)
    print(f"you have selected :{vip_drink} successfully")


else:
    print("invalid age")

    pass
