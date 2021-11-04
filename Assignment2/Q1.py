def judge(s):
	if [k for k in s.split() if not k.isdigit()]:
		return []
	else:
		return list(map(int,s.split()))
	
def getValues(): #keep input until the input is suitable
    while True:
        ints = judge(input('a b: '))
        if len(ints) == 2:
            a, b = ints
            if 0 < a < b:
                break
    while True:
        divisors = sorted(set(judge(input('Divisors: '))))
        if len(divisors) >= 1:
            if not [d for d in divisors if not 0 < d <= b]:
                break
    return a, b, divisors

def main():
	a, b, divisors = getValues()
	print('M', ' '.join(map(str, divisors)))
	for i in range(a,b):
		print(i, ' '.join(['1' if i % d == 0 else '0' for d in divisors]))

main()