a=10;b=20
print(f"and {a<10 and a<b}")
print(f"or {a<10 or a<b}")
print(f"not {not(a<b)}")
print(f"and {a<10 and a/0}")
print(f"and {a<11 and a/0}")

#output
'''and False
or True
not False
and False
Traceback (most recent call last):
  File "boolean_operators.py", line 6, in <module>
    print(f"and {a<11 and a/0}")
ZeroDivisionError: division by zero'''



