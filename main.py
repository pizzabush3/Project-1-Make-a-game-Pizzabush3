import time
import random
repeat = 0
violence = 0
boredom = 0
loopHap = 0

print("Hello! welcome to dumb ways to live!")
time.sleep(3)
print("I am your sentient dog named Loopy Doopy")
time.sleep(3)
print("currently, you are in a cave with no visible exits")
time.sleep(3)
while True:
  repeat += 1
  print("what do you do? you see a beartrap, a perpetual motion machine, and a very sharp pencil")
  time.sleep(2)
  modifier = random.randint(1,3)
  if modifier == 1:
    beartrap = ("play with")
    perpetual = ("observe")
    pencil = ("step")
  if modifier == 2:
    beartrap = ("step on")
    perpetual = ("play with")
    pencil = ("observe")
  if modifier == 3:
    beartrap = ("observe")
    perpetual = ("step on")
    pencil = ("play with")
 
  Choose = (int(input(f"{beartrap} the beartrap(1) {perpetual} the perpetual motion machine(2) {pencil} the very sharp pencil(3) pet loopy(4)")))
  if Choose == 1:
      if violence >= 3:
        print(f"you {beartrap} the beartrap, and it snaps shut on you and you die eventually from blood loss")
        print("loopy: I was supposed to save you, but since you keeping trying to hurt yourself and being annoying I suppose I shoudn't save you")
        print("loopy:I guess thats a way to break out of the loop")
        break
      elif beartrap == "step on" or beartrap == "play with":
        violence += 1
        print(f"As your about to {beartrap} it, the beartrap snaps shut")
        time.sleep(3)
        print("Loopy doopy: Hey! don't step on that! hurting yourself is bad")
        time.sleep(3)
      else:
        time.sleep(2)
        print("you observe the beartrap")
        time.sleep(3)
        print("you fall asleep from boredom")
        boredom += 1
        time.sleep(3)
  elif Choose == 2:
    if perpetual == "observe" or perpetual == "play with":
      print(f"you {perpetual} with the perpetual motion machine") 
      time.sleep(5)
      boredom += 1
      print("you fall asleep from boredum")
      time.sleep(2)
    elif perpetual == "step on":
      print("you step on the perpetual motion machine")
      time.sleep(3)
      print("loopy: WHY DID YOU STEP ON MY PERPETUAL MOTION MACHINE???")
      time.sleep(3)
      print("what do you say?")
      Why =(int(input("It was an accident(1) I just wanted too(2) you are annoying(3)I don't know(4)")))
      if Why == 1 or Why == 4:
        print("loopy: yeah right, I don't belive that")
        violence += 10
      elif Why == 2 or Why == 3:
        print("loopy:thats true, ")
        time.sleep(3)
        if boredom >= 5:
          loop = input("loopy:are you bored of being in this loop? yes/no")
        elif boredom < 5:
          print("you don't seem bored enough yet")
          if loop == "yes" and loopHap >= 2:
            leave = input("loopy:do you want to leave? yes/no")
            if leave == "yes":
              print("ok, bet")
              time.sleep(2)
              print("you also are pretty nice to me so I will let you escape the loop")
              time.sleep(5)
              break
            elif leave == "no":
              print("ok bet")
              time.sleep(2)
            else:
              print("that is not a valid answer")
          elif loop == "no":
            print("ok, bet")
            time.sleep(2)
          else:
            print("that is not a valid answer")
            time.sleep(3)
        else:
          print("that is not a valid answer")
      else:
        print("that is not a valid answer")
        time.sleep(3)
          
  elif Choose == 3:
    if pencil == "step on":
      if violence >= 3:
        print(f"you {pencil} the sharp pencil and die from blood loss")
        time.sleep(5)
        print("loopy:I was going to save you, but you keep trying to hurt youself and were being annoying")
        time.sleep(5)
      else:
        violence += 1
        time.sleep(3)
        print("loopy:Hey! don't do that, hurting yourself is bad") 
        time.sleep(2)
    elif pencil == "observe" or pencil == "play with":
      print(f"you {pencil} the pencil")
      time.sleep(3)
      print("eventually you fall asleep from boredom")
      boredom += 1
      time.sleep(3)
  elif Choose == 4:
    time.sleep(0.5)
    print("you pet loopy")
    time.sleep(1)
    print("loopy seems to enjoy it")
    time.sleep(2)
    loopHap += 2
    
  else:
    print("not a valid answer")
print("yay you escaped!")
time.sleep(2)
print("there are multiple endings to get")
time.sleep(2)
print("play again to find them all")
    
  