word = "aabb"
sonuc = -1
sayac = {}
for i in range(len(word)):
    if word[i] in sayac:
        sayac[word[i]] += 1
    else:
        sayac[word[i]] = 1
print(sayac)

for j in range(len(word)):
    if sayac[word[j]] == 1:
        sonuc = j
        break
print(sonuc)
