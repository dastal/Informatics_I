def make_dice(x):
    single_probability = 1 / x
    return lambda x: single_probability ** x

die_with_6_nums = make_dice(6)
die_with_3_nums = make_dice(3)

print(die_with_6_nums(2))
print(die_with_3_nums(2))