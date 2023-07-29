print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print('You show up to the climbing gym and some gumbies are projecting your warm up problem.')
choice1 = input('type "flash" to flash their project. type "move on" to find another probem to warm up on.\n')
if choice1 == 'flash':
  print("your foot slipped and you accidentally fell off the 2nd move of a v2. All the gumbies say 'aww dont worry dude, its a rough problem'.\nYou take your own life in shame.\nGAME OVER.")
elif choice1 == 'move on':
  print('you approach 2 groups of climbers working different problems. One is delicate slab and the other is powerfull overhang.')
  choice2 = input('Type "slab" to join the slab group. Type "overhang" to join the overhang group\n')
  if choice2 == 'overhang':
    print('You silly boulder bro. You absolute fool. In your desire to look cool you ignored the fact that slab is your weakness and you really need to work on it. You die a sad old boulder bro, riddled with injuries and incapable of becoming the gracfully aging "trad dad".\nGAME OVER (sad and alone ending)')
  elif choice2 ==  "slab":
    print('You join the group of slab climbers who are of course naturally attractive and super funny. You immidiatly eat shit infront of them and cheese grate down the entire 15 ft slab (its really easy too [very embarssing for you])')
    choice3 = input('Type "casual" to play it off like its no biggie. Type "barf" to throw up in total embarssment and social anxiety\n')
    if choice3 == 'casual':
      print('oh no.. the super hot and funny slab climbers saw straight through your attempt to be casual and think youre a poser who cant even be real about their feelings. They constantly suggest that you need to go to therapy, withought providing any meaningful way to take a first step untill you pass out. You later die as a resut of your injuries\nGAME OVER')
    elif choice3 == 'barf':
      print('you go to barf but just sit ther and dry heave like an idiot for like 3 minutes as all the slab climbers (hot and super funny) stare at you. After you gain your composure they all clap and cheer. They love how emotionally vulnerable your dry heaving was and they want to be your friends!\nYOU WIN.\nThe treasure was the hot and funny slab climbing friends we made along the way.')