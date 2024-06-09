def likes(names):
    # your code here
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return f"{names[0]} likes this"
    elif len(names)<4:
        return ", ".join(names[:-1])+" and "+names[-1]+" like this"
    else:
        return ", ".join(names[:2])+f" and {len(names)-2} others like this"
        