import os, time, random
grandpaOutside = random.randint(0, 1)  # Variable 1
noorChosen = 0                         # Variable 2
name = input("Enter your name:  ")     # Variable 3
def say(text: str):  
  print ("\033[1;37m" + text)

# "\033[1;37m" + name + "\033[0m" Bolds the Name

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome explorers! You are the character " + "\033[1;37m" + name + "\033[0m" + " navigating through \033[1;37myour crazy grandmas house\033[0m")
  print()
  print()
  print("Let's get started!")
  time.sleep(3.5) # wait 3 seconds before moving on
  noor1() # runs to send the player to noor #1
  pass

def noor1():
  os.system('clear')
  print("Your grandma has been planning to kill you and your siblings.")
  time.sleep(3.5)
  os.system('clear')
  print("Choose which path to take to escape")
  time.sleep(3.5)
  os.system('clear')
  print("The room has a window and a noor")
  time.sleep(3.5)
  os.system('clear')
  noorChosen = input("Choose 1 to try to escape through the noor and 2 to try to escape through the window :  ")
  if noorChosen == 1:
    noor2()
  else:
    noor3()
  pass
def noor2():
  os.system('clear')
  print("You try to open na noor but the door was booby trapped, ")
  time.sleep(3.5)
  os.system('clear')
  endGame()
  pass
  

def noor3():
  os.system('clear')
  if grandpaOutside == 1:
    print("Your grandfather is working in the garden and sees you trying to escape")
    time.sleep(3.5)
    os.system('clear')
    print("Not wanting to anger grandma he rushes inside and pulls you to the ground")
    time.sleep(3.5)
    os.system('clear')
    print("The window had a padlock on it anyways, but now your chances of escape are slim")
    time.sleep(3.5)
    os.system('clear')
    print("grandpa locks you in the basement")
  else:
    time.sleep(3.5)
    os.system('clear')
    print("You try to escape through the window but its padlocked and grandma catches you and throws you in the basement")
  noor4()
  pass

def noor4():
  time.sleep(3.5)
  os.system('clear')
  print("your grandparents decide you have been too much work and" 
+ "\033[1;37m" + " Get Rid Of You" + "\033[0m")
  endGame()
  pass

def endGame():
  time.sleep(3.5)
  os.system('clear')
  print("You just die there screaming 'OPEN NA NOOR' with your grandparents standing over you while they talk about consuming your corpse")
  pass

startGame()