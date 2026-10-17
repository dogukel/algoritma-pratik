def valid_anagram(s, t):
    sayac_s = {}
    sayac_t = {}
    if len(s)!= len(t):
        return False
    for i in range(len(s)):
        if s[i] in sayac_s:
            sayac_s[s[i]]+=1
        else:
            sayac_s[s[i]]=1
        if t[i] in sayac_t:
            sayac_t[t[i]]+=1
        else:
            sayac_t[t[i]]=1
    return sayac_s == sayac_t

print(valid_anagram("elma", "lame")) 
print(valid_anagram("aab", "abb"))  
print(valid_anagram("ab", "abc"))   