#The game() function in a program lets a user play a game and returns the score as an integer.
#you need to read a file 'hiscore.txt' which is either blank or contains the previous high score.
#write a program to update the high score whenever game() breaks the high score.

def game():
    return 80

score  = game()
with open('D:\\Python\\Python_Programs\\06_File\\highscore.txt') as f: #open a file
    highscore = f.read()
    if highscore == "":
        with open('D:\\Python\\Python_Programs\\06_File\\highscore.txt', 'w') as f:
            f.write(str(score))
    elif(int(highscore) < score):
        with open('D:\\Python\\Python_Programs\\06_File\\highscore.txt', 'w') as f:
            f.write(str(score))
