def specialArray(nums):
        n = len(nums)
    
        for x in range(n + 1):
            kat_teng = sum(1 for num in nums if num >= x)
            
            if kat_teng == x:
                return x
        
        return -1
    
nums = [3, 5, 2, 0, 4, 1]

print(specialArray(nums))