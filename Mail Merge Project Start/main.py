# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode='r') as file:
    names = file.readlines()

for i in range(0, len(names)):
    names[i] = names[i].replace('\n', '', )

for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode='w') as output:
        with open("./Input/Letters/starting_letter.txt", mode='r') as file:
            letter = file.readlines()
            letter[0] = letter[0].replace('[name]', f"{name}")
        output.writelines(letter)
