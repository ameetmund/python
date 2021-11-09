nums = [1, 1, 2]


class Solution:
    def removeDuplicates(self, nums):
        new_list = list(set(nums))
        return(new_list)


sol = Solution()
sol.removeDuplicates(nums)

