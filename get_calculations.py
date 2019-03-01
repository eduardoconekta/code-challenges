def  get_calculation( number ):
    flag = True
    tmp_number = 1
    invalid = 0
    operations = ["1"]
    while flag:
        if tmp_number >= number:
            flag = False
        if invalid == 2:
            flag = False
            operations = ["invalid input"]
            continue

        if tmp_number * 3 <= number:
            operations.append("* 3")
            action_before = tmp_number
            tmp_number = tmp_number * 3
            continue

        if tmp_number + 5 <= number:
            operations.append("+ 5")
            action_before = tmp_number
            tmp_number = tmp_number + 5
            continue

        if action_before + 5 <= number:
            operations.pop()
            tmp_number = action_before
            operations.append("+ 5")
            tmp_number = tmp_number + 5 
            invalid = invalid + 1 
            continue
        
        
    return ' '.join(operations)

print get_calculation(106) 
print get_calculation(6) 
print get_calculation(7) 
