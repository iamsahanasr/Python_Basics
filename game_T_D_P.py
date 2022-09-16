start_state="""
   ___ ___
  | T | D |
  |___|___|
  |   | P |
  |___|___|
"""
killed_state="""
   ___ ___
  | T | D |
  |___|___|
  |   |   |
  |___|___|
  Game Over you are killed
"""

mid_state="""
   ___ ___
  | T | D |
  |___|___|
  | P |   |
  |___|___|
"""

win_state="""
   ___ ___
  | P | D |
  |___|___|
  |   |   |
  |___|___|
  You Win
"""
print(start_state)
input1=input("enter the U key for Up and L key for Left R key for Right D key for Down\n")
if input1=="U" or input1=="u":
    print(killed_state)
   
elif input1=="L" or input1=="l":
    print(mid_state)
    move=input("enter the key\n")
    if move=="U" or move=="u":
        print(win_state)
    else:
        print("invalid key")

   
else:
    print("invalid key")



