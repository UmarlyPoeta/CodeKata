def persistence(n):
    counter = 0 
    
    while len(str(n)) > 1:
        new_num = 1
        for single_num in [int(i) for i in str(n)]:
            new_num *= single_num
        n = new_num
        counter += 1
    
    return counter