def hex_string_to_RGB(hex_string): 
    # your code here
    return {"r":int(hex_string[1:3],16),"g":int(hex_string[3:5],16),"b":int(hex_string[5:],16)}