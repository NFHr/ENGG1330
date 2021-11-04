str1 = input('string 1: ')
str2 = input('string 2: ')
i,j = 0, 0
list1 = []

while i < len(str1):
    if str2[i:i+len(str2)] == str2:
        j += 1
    i += 1

print(j)