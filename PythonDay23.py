l = [2, 4, 452, 69, 5, 6, 7, 8]
print(l)
l.append(45)
# l.sort(reverse=True)
l.reverse()
print(l)
print(l.count(4))

s = l.copy()
s[0] = 69
print(s, l)

l.insert(2, "AAAAAAAAAAAAAAAAAAA")
print(l)

m = ["sigma", "ligma", "sawcon"]
l.extend(m)
print(l)
k = ["AAAAAAAAAAAAAAA", "GAAAAAAAAAAAAAAAAAA"]
k = l + m
print(k)