# Day 2 - Tip Calculator

print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
percent = input('What percentage tip would you like to give? 10, 12, or 15? ')
people = input('How many people to split the bill? ')

bill_with_tip = int(percent) / 100 * float(bill) + float(bill)
per_person = round(bill_with_tip / int(people), 2)

print(f'Each person should pay: ${per_person}')