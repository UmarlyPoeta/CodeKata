def solution(number):
    d=3
    f=5
    tab=[]
    while d<number:
        tab.append(d)
        d+=3
    while f<number:
        tab.append(f)
        f+=5
    return sum(set(tab))
        