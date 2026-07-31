# # def cube(x):
# #     return x*x*x
# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

# # use of MAP
# newl = list(map(lambda x: x**3, l))
# print(newl)

# # use of FILTER
# def filter_function(a):
#     return a > 2

# newNewl = list(filter(filter_function, l))
# print(newNewl)

# use of REDUCE

from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]

sum = reduce(lambda x, y: x + y, numbers)
# working of the function:
# [1, 2, 3, 4, 5, 6] (1 + 2 are added, remaining list: [3, 3, 4, 5, 6])
# [3, 3, 4, 5, 6] (3 + 3 are added, remaining list: [6, 4, 5, 6])
# [6, 4, 5, 6] (6 + 4 are added, remaining list: [10, 5, 6])
# [10, 5, 6] (10 + 5 are added, remaining list: [15, 6])
# [15, 6] (15 + 6 are added, remaining list: [21])

print(sum)