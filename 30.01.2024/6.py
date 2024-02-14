n = int(input("Nechta qator IP address kiritiasiz: "))
nums = list()
nums2 = list()
for i in range(n):
    num = input(f"{i + 1} - IP addressni kiriting_(125.199.45.22): ")
    nums2.append(num)
    ls = num.split(".")
    nums.append(ls)
print("\n")
    
def formula(nums2, nums):
    ls = list()
    count = 3
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            sum += (int(nums[i][j]) * pow(256, count))
            count -= 1
        ls.append(sum)
        sum = 0
        count = 3
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
                nums2[i], nums2[j] = nums2[j], nums2[i]
        print(nums2[i])
                

formula(nums2, nums)
