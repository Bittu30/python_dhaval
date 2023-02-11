# this is the excercise for the dict and tuple

friend = ['nka', 'fishf', 'hfsuhfwis', 'njdfjd']

friend_age = ('nak', 6, 'fisijhd', 12, 'gfsgf', 10)

print(friend_age)

exp = {"clothes": 1100, "shoes": 1000, "watch": 900, "mobile_recharge": 1100, "petrol_recharge": 1980}

total = 0

for i in exp.values():
    total = total + i
print(total)

wife_exp = {"clothes": 2310, "shoes": 999, "watch": 900, "mobile_recharge": 799, "makeup": 3670, "dth_recharge": 999}


wife_total=0

for i in wife_exp.values():
    wife_total = wife_total+i

print(wife_total)

print(wife_total-total)

