rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
outcomes = [rock,paper,scissors]
RPS = int(input('Type 1 for rock\n     2 for paper\n     3 for scissors\n'))-1
Computer_RPS = random.randint(0,2)
print(outcomes[RPS])

if RPS == Computer_RPS:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nDRAW!")
elif RPS == 0 and Computer_RPS == 1:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou lose")
elif RPS == 0 and Computer_RPS == 2:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou win")
elif RPS == 1 and Computer_RPS == 2:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou lose")
elif RPS == 1 and Computer_RPS == 0:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou win")
elif RPS == 2 and Computer_RPS == 0:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou lose")
elif RPS == 2 and Computer_RPS == 1:
  print(f"Computer chose:\n{outcomes[Computer_RPS]}\nYou win")
