class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)
        
        for i in range(0, zero_count):
            nums.remove(0)
            nums.append(0)
            