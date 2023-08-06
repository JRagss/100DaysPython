############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from art import logo
from replit import clear

# Determine if the user is holding an ace and is above or below 21 to change its value.
def adv_hand_total(hand):
  total = sum(hand)
  while total > 21 and 11 in hand:
    hand[hand.index(11)] = 1
    return sum(hand)
  return sum(hand)

# Special print function which encases the text in a dashed line box
def border_print(string):
  border = ["+"]
  for characters in range(len(string)+2):
    border.append("-")
  border.append("+")
  border =''.join(border)
  print(border+"\n"+"| "+string+" |\n"+border)

# Determine if the user won or lost and print the correct statment to the user in a border print
def win_or_lose(player_total,computer_total):
  if player_total > 21:
    border_print("You went over, you lose.")
  elif computer_total > 21 and player_total < 21:
    border_print("You win!")
  elif player_total == 21 and computer_total != 21:
    border_print("You win!")
  elif 21-player_total >0 and 21-player_total> 21-computer_total:
    border_print("You lose.")
  elif 21-player_total >0 and 21-player_total< 21-computer_total:
    border_print("You lose.")
  elif player_total == computer_total:
    border_print("It's a draw")


# Primary blackjack loop function
def blackjack():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # Randomly pick a hand for the user and computer assuming an infinite number of decks
  user_hand = random.choices(cards, k=2)
  npc_hand = random.choices(cards, k=2)

  # Variables to display only the compters first card to the user
  npc_display_hand = npc_hand
  npc_display_total = npc_display_hand[0]

  # Determine current total scores of thet user and computer
  user_total=adv_hand_total(user_hand)
  npc_total=adv_hand_total(npc_hand)
  
  # Display the users starting hand and score. Dispaly the computers first card and it's "score"
  print(f"Your cards: {user_hand}, current score:{user_total}")
  print(f"Computers first card: {npc_display_hand[0]}, current score:{int(npc_display_hand[0])}")
  
  #in a loop, ask the player if they want a new card or not, check for score, update player hand. 
  hit_stand = True
  while hit_stand:
    #If the users score is over 21 break the loop
    if user_total > 21:
      hit_stand = False
      break
    new_card = input("Would you like aother card? y/n: ")
    
    # If the player selects a new card, add that card to their hand, find a new total score and display both.
    if new_card == "y":
      user_hand.append(random.choice(cards))
      user_total = adv_hand_total(user_hand)
      print(f"\nYour hand: {user_hand}, Your score:{user_total}")
      print(f"Computer score: {npc_display_total}")
      
    # If the player does not want a new card exit the loop.
    elif new_card == 'n':
      hit_stand = False
  
  #computer taking cards while under 17
  if user_total <= 21:
    while npc_total < 17:
      npc_hand.append(random.choice(cards)) 
      npc_total = adv_hand_total(npc_hand)

  # Display final totals and hands.
  print(f"\nYour final score: {user_total}")
  print(f"The computers final hand: {npc_hand}, final score: {npc_total}")

  # Determine win or loss
  win_or_lose(user_total,npc_total)

  # Ask if the player wants a new game, if yes clear the consol and re-call blackjack function. Else continue
  again_input = input("\nWould you like to play another game? y/n: ")
  if again_input == 'y':
    clear()
    blackjack()


#border_print("Test String      To ... print")
blackjack()

border_print("Thanks for playing my game!")