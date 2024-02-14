def intersection(nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        res = list(set1.intersection(set2))
        
        return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))