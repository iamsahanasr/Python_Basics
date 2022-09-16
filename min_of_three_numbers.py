num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

min_of_two=num1 if num1<num2 else num2
min_of_three=min_of_two if min_of_two<num3 else num3
print(f"min of {num1} {num2} and {num3} is {min_of_three}")

'''
output:-

enter the first number
2
enter the second number
5
enter the third number
1
min of 2 5 1 is 1
'''
