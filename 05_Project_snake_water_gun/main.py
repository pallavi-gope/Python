#Snake, Water, Gun Game or Roc,k Paper, Scissor

import random

def game(comp, you):
    #if both values are equal, game will tie 
    if comp == you:
        return None
    #check all possibilities
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    #check for water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #check for gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# p1 = input("Comp Turn : Snake(s), Water(w) or Gun(g) ?")
randVal = random.randint(1, 3)

if(randVal == 1):
    comp = 's'
elif(randVal == 2):
    comp = 'w'
elif(randVal == 3):
    comp = 'g'

p2 = input("Your Turn : Snake(s), Water(w) or Gun(g) ?")

print(f"Computer Choose : {comp}")
print(f"You Choose : {p2}")

result = game(comp, p2)

if result == None:
    print("The Game is Tie!")
elif result:
    print("You Win!")
else:
    print("You Lose!")
