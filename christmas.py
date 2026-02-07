
#8. Tip, Tax, and Total
meal_charge = float(input('Enter meaal price: $'))

#calculate tip
tip = meal_charge * 0.18
print('Tip:', tip)

#calculate tax
tax = meal_charge * 0.07

#calculate total
total = meal_charge * tip * tax

#Display results
print('Tip Amount: ', tip)
print('Tax Amount: ', tax)
print('Total Amount:', total)

#11. Lion and Tiger Percentages
lions = int(input('Enter the number of lions: '))
tigers = int(input('Enter the number of tigers: '))

total_cats = lions + tigers

#calculate # of lions
lion_percentage = lions / total_cats
#calculate # of tigers
tiger_percentage = tigers / total_cats
#Display results
print(f'Percentage of Lions at the Exhibit: {lion_percentage:.0%}')
print(f'Percentage of Tigers at the Exhibit: {tiger_percentage:.0%}')