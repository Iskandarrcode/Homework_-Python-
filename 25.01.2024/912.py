from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result

nums = [5, 2, 3, 1]
sol = Solution()
sorted_nums = sol.sortArray(nums)
print(sorted_nums)
