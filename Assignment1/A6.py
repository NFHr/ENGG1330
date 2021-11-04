stairs = int(input())
case = [0] * (stairs)
pset = [1]

for n in range(2,stairs+1):
   m=2
   for m in range(2,n):
      if(n%m==0):
         break
   else:
      pset.append(n)

for i in range(stairs):
    if i+1 in pset:
        case[i] = case[i] + 1
    for j in pset:
        if i < j:
            break
        case[i] = case[i] + case[i-j]

print(case[-1])