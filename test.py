def em_buy (N, row):
    current_sum = 0
    greatest_sum = 0
    for emerald in row: 
        if emerald % 2 == 0:
            current_sum += emerald
            if current_sum > greatest_sum:
                greatest_sum = current_sum
        if emerald % 2 != 0:
            current_sum = 0
    print(greatest_sum)
em_buy(13,[2,3,4,4,5,6,1,2,2,2,1,8,2])