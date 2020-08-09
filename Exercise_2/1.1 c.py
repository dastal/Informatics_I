number_adults = int(input('How many adults are there? '))
print(number_adults)
number_children = int(input('How many children are there? '))
print(number_children)
delivery = str(input('Do you want your pizzas delivered? (True or False) '))

total_pizza = number_adults + number_children
total_price = 0
individual = 10
child = 6
price_drop = 0.8
birthday = -10
price_drop_birthday = 0.8 * -10
delivery_price = 5

if (total_pizza >= 20) and (delivery == "False"):
    total_price = total_price + number_adults * individual * price_drop + number_children * child + price_drop_birthday
elif (total_pizza >= 20) and (delivery == "True"):
    total_price = total_price + number_adults * individual * price_drop + number_children * child + price_drop_birthday + delivery_price
elif ((number_adults > 0) or (number_children > 0)) and (delivery == "False"):
    total_price = total_price + number_adults * individual + number_children * child + birthday
elif ((number_adults > 0) or (number_children > 0)) and delivery == "True":
    total_price = total_price + number_adults * individual + number_children * child + price_drop_birthday + delivery_price
else:
    print('Default')

print('Total cost: CHF', int(total_price))