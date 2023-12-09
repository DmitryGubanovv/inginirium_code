def c_s_b(input_string):
    l = 0
    r = 0
    for s in input_string:
        if "(" in s:
            l+=1
        if ")" in s:
            r+=1
        if 

    if l == r:
        print("yes")
    else:
        print("no")
c_s_b(")(")