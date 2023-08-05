from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


more_biders = True
bids = {}
while more_biders == True:
  print(logo)
  print("Welcome to the secret auction program.")
  
  name = input("What is your name?: ").lower()
  amount = int(input("What is your bid?: $"))

  bids[name] = amount

  more_biders_question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if more_biders_question == 'no':
    more_biders = False
  clear()
#key = name: bid = value

highest_bid = 0
for key in bids:
  if bids[key] > highest_bid:
    highest_bid = bids[key]
    winner = key
    tied_biders = []
  elif bids[key] == highest_bid:
    tied_biders.append(key)


print(logo)
if not tied_biders:
  print(f"The winner of the silent auction is {winner} with a bid of ${highest_bid}")
else:
  print(f"The following people have tied with the same bid of ${highest_bid}")
  for name in tied_biders:
    print(name)
  print(winner)