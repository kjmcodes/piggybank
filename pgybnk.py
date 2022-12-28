def payment(amount):
    val1 = len(str(amount))
    val2 = (int((str(amount))[0]))
    if val1 == 2:
        val3 = (val2 + 1) * 10
        val3 - amount
        # print (val4)
    elif val1 == 3:
        val3 = (val2 + 1) * 100
        val4 = val3 - amount
        # print (val4)
    elif val1 == 4:
        val3 = (val2 + 1) * 1000
        val4 = val3 - amount
        # print (val4)
    elif val1 == 5:
        val3 = (val2 + 1) * 10000
        val4 = val3 - amount
        # print (val4)
    else:
        print ("Unfortunately, Piggybank savings are only available for amounts above $10 but below $100,000")

payment (97)

