

List = [1,2,3,4,5,6,7]

class Solution:
    def rotate(self, nums, k) -> None:
        def reverse(self, nums):
            end_val = nums[-1]
            nums.pop()
            nums.insert(0,end_val)
            return nums
        for i in range(0,k):
            nums = reverse(self,nums)




def main():
    s = Solution

    s.rotate(s,List,2)

    print(List)


main()