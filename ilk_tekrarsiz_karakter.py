def ilk_tekrarsiz_karakter(word):
    sonuc = -1
    sayac = {}
    for i in range(len(word)):
        if word[i] in sayac:
            sayac[word[i]] += 1
        else:
            sayac[word[i]] = 1
    
    for j in range(len(word)):
        if sayac[word[j]] == 1:
            return j
    return sonuc
print(ilk_tekrarsiz_karakter("leetcode"))      
print(ilk_tekrarsiz_karakter("loveleetcode"))  
print(ilk_tekrarsiz_karakter("aabb")) 