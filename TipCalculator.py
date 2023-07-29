#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
cost = float(input("What was the total cost of the meal?\n$"))
num_people = int(input("How many people will be splitting the bill?\n"))
percentage = float(input("What percentage tip would you like to give? 15, 18, 20\n") )#the suggested tips in the video are awful


cost_per_person = (cost/num_people) * (percentage/100+1)
rounded_cost_per_person = round(cost_per_person,2)
print("Each person should pay ${:.2f}".format(rounded_cost_per_person))