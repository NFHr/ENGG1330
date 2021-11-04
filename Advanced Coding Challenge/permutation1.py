def perm(nums):
    i,j = len(nums) - 2, len(nums) - 1

    while int(nums[i]) > int(nums[i+1]):
        i -= 1

    while int(nums[i]) > int(nums[j]):
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]

    nums[i+1:len(nums)] = list(reversed(nums[i+1:len(nums)]))

    if i < 0:
        return False
    return True

def main():
    nums = input().split()
    print(nums)
    while perm(nums):
        print(nums)
main()