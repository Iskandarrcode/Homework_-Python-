nums = [0, 1]

def Missing_num(nums):
    l = len(nums)
    for i in range(1, l + 1):
        if i not in nums:
            return i
        
print(Missing_num(nums))