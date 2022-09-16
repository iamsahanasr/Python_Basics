num1=int(input("enter the first number\n") or 0)
num2=int(input("enter the second number\n") or 0)

msg="less" if num1<num2 else "greater or equal"
print(msg)

'''
output:-

enter the first number

enter the second number
2
less

enter the first number
2
enter the second number

greater or equal
'''
