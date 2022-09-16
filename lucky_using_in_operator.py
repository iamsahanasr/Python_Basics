num1=input("enter the number\n")
decision="95" in num1 or "5" in num1
msg="lucky" if decision==True else "unlucky"
print(msg)

'''
output:-
enter the number
123456
lucky

enter the number
1234595467
lucky

enter the number
1234678
unlucky
