
num1=float(input("enter the first number\n"))
num2=float(input("enter the second number\n"))
i=0
num=0
numdeci=0
numint=int(num2)
decimal=num2-numint
print("the integer part is",numint)
print("the decimal part is",decimal)
while i<num1:
    num=num+numint
    numdeci=numdeci+decimal
    i+=1
print(num)
print(numdeci)
print("the product is",num+numdeci)
