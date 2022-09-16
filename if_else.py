# height=float(input("Enter your height"))
# weight=int(input("Enter your weight"))
# if height>=5.5 and weight>=50:
#     print("You are eligible for army")
# elif height<5.5 and weight>=50:
#     print("You are not eligible for army as your height is less than requirements")
# elif height>=5.5 and weight<50:
#     print("You are not eligible for army as your weight is less than requirements")
# else:
#     print("You are not eligible for army as both height and weight are less than requirements")

# #else always binds with nearest if statement

# height=float(input("Enter your height"))
# weight=int(input("Enter your weight"))
# if height>=5.5 and weight>=50:
#     print("You are eligible for army")
# elif height<5.5:
#     print("You are not eligible for army as your height is less than requirements")
# elif weight<50:
#     print("You are not eligible for army as your weight is less than requirements")
# else:
#     print("You are not eligible for army as both height and weight are less than requirements")


# height=float(input("Enter your height"))
# weight=int(input("Enter your weight"))
# if height>=5.5:
#     if weight<50:
#         print("Weight is less than requirements")
#     else:
#         print("you are eligible for army")
# else:
#     if weight<50:
#         print("Both Height and Weight is less than requirements")
#     else:
#         print("Height is less than requirement")


height=float(input("Enter your height"))
weight=int(input("Enter your weight") or 45) #empty string in boolean context are evaluated as false

if height>=5.5:
    if weight<50:
        print("Weight is less than requirements")
    else:
        print("you are eligible for army")
else:
    if weight<50:
        print("Both Height and Weight is less than requirements")
    else:
        print("Height is less than requirement")
