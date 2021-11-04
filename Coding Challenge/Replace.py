str, chr, n= input('string: '), input('character: '), 1
list1 = []
for i in str:
    list1.append(i)
for j in range(len(list1)):
    if str[n] == chr:
        list1[n] = j
        j += 1
    if j == 9:
        break

for m in list1:
    print(m, end='')
    
print()