#Stone Paper Scissor Game
import random
def gameWin(Comp,you):
 if Comp == you:
   return None
 elif Comp =='P':
  if you == 'St':
   return False
  elif you == 'S':
        return True
  elif Comp == 'St':
   if you == 'S':
    return False
 elif you == 'P':
  return True
 elif Comp == 'S':
   if you == 'P':
     return False
   elif you == 'St':
     return True
   
print("Comp Turn: Stone(St), Paper(P) or Scissor(S)?")
randNo = random.randint(1, 3)
if randNo == 1:
     Comp = 'P'
elif randNo == 2:
     Comp = 'St'
elif randNo == 3:
     Comp = 'S'

you = input("Your Turn: Stone(St), Paper(P) or Scissor(S)?")
a = gameWin(Comp, you)
print(f"Computer chose {Comp}")
print(f"You chose {you}")
if a == None:
       print("The game is a Tie!")
elif a:
       print("You Win!")
else:
       print("You Loose!")      
