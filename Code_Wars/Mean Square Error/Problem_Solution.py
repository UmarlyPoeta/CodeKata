
def solution(array_a, array_b):
    array_diff = []
    for i in range(len(array_a)):
        array_diff.append(pow(abs(array_a[i]-array_b[i]),2))
    return sum(array_diff)/len(array_diff)