nums = list(map(int,input('Numbers: ').split(',')))
new = []

for _ in range(len(nums)):
    temp = nums[0]
    for i in range(len(nums)):
        if nums[i] > temp:
            temp = nums[i]
    new.append(temp)
    nums.remove(temp)

new = list(map(str,new))

print(' '.join(new))