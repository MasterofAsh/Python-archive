# Reading a file

# f = open('testAbdullah.py', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# Writing a file

f = open('testAbdullah.txt', 'w')
f.write("Hello world")
f.close()

with open('testAbdullah.txt', 'a') as f:
    f.write("Hey, I am inside the file using with")