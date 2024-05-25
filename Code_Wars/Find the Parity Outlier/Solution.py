def find_outlier(integers):
    even=[i for i in integers if i%2==0]
    odd=[i for i in integers if i%2!=0]
    if len(even)>len(odd):
        return odd[0]
    else:
        return even[0]