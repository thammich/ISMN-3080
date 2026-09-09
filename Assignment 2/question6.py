is_member = False
items_purchased = 3

if (is_member and items_purchased >= 5):
    print("Bonus")
elif (is_member or items_purchased >= 10):
    print("Standard")
else:
    print("Basic")