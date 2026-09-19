class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float('infinity')

        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            l , r = i + 1, len(nums) - 1

            while l < r :
                threesum = nums[i] + nums[l] + nums[r]

                if abs(threesum - target) < abs(closest - target):
                    closest = threesum
                if threesum <= target:
                    l += 1
                elif threesum > target:
                    r -= 1
        return closest