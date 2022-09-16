find=input("Enter letter or number or special characters\n")
if find in ("a","e","i","o","u","A","E","I","O","U") :
    print(f"{find} is vowel")
elif "0"<=find<="9":
    print(f"{find} is number")
elif find in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print(f"{find} is consonant")
else:
    print(f"{find} is Special Symbol")

# inbetween operator 'a'<= letter<='z'
                    #  letter>='A' and letter<='Z'