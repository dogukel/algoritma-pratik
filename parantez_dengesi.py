def parantez_dengeli(s):
    esler = {")":"(", "]" :"[", "}":"{"}
    yigin = []
    for harf in s:
        if harf in "([{":
            yigin.append(harf)
        else:
            if len(yigin) == 0:
                return False
            if yigin[-1]!= esler[harf]:
                return False
            yigin.pop()
    return len(yigin) == 0

print(parantez_dengeli("([]{})"))
print(parantez_dengeli("([)]"))    
print(parantez_dengeli("(("))      
print(parantez_dengeli(")"))  