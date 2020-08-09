def product_of_two_or_three_numbers(num_1, num_2, num_3=1):
    product = num_1 * num_2 * num_3
    print("The product of {0:d}, {1:d} and {2:d} is {3:d}.".format(num_1,num_2,num_3,product))


product_of_two_or_three_numbers(3,4,2)
product_of_two_or_three_numbers(3,4)

# num_3 is only used when its needed. So I programmed num_3 as a keyword argument and assigned it the value 1,
# so that it won't distort the result.