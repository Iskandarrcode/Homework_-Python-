nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = 3

def sorts(nums1, nums2, n):
    nums1.extend(nums2)
    for i in range(n):
        nums1.remove(0)
    
    for i in range(len(nums1)):
        for j in range(i + 1, len(nums1)):
            if nums1[i] > nums1[j]:
                nums1[i], nums1[j] = nums1[j], nums1[i]
    return nums1
            

print(sorts(nums1, nums2, n))