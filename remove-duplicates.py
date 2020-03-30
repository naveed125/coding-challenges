import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return 1
        
        prev = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == prev:
                del nums[i]
            else:
                prev = nums[i]
                i += 1

        return len(nums)


if __name__ == '__main__':

    print(Solution().removeDuplicates(sys.argv.copy()[1:]))
