dna = input('DNA: ')
pattern = input('Pattern: ')
i = 0
list1 = []

while i < len(dna):

    if dna[i:i+len(pattern)] == pattern:
        list1.append('*')
    else:
        list1.append('_')
    i += 1
print(dna)
for m in list1:
    print(m, end='')
print()