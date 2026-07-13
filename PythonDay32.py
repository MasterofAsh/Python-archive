# s1 = {1, 7, 9}
# s2 = {2, 4, 6, 5, 9}
# # print(s1.intersection(s2))
# s1.update(s2)
# print(s1, s2)

cities1 = {"karachi", "rawalpindi", "tokyo"}
cities2 = {"islamabad", "rawalpindi", "karachi"}
# cities3 = cities1.intersection_update(cities2)
cities1.add("Multan")
item = cities2.pop()
print(item)