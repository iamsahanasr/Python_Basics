
num=int(input("enter the number"))
last_digit=num%10
result="even" if last_digit in (0,2,4,6,8) else "Odd" #tuple
print(result)

num=int(input("enter the number"))
last_digit=num%10
result="even" if str(last_digit) in "02468" else "Odd" #tuple
print(result)


