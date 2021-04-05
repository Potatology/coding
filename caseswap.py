import string

def swap_case(s):
    slist=[s]
    for c in slist:
        if c in string.ascii_uppercase:
            slist[c.lower()]
        elif c in string.ascii_lowercase:
            slist[c.upper()]
        else: continue
        
    return str(slist)


print(swap_case('AsasasAAA'))