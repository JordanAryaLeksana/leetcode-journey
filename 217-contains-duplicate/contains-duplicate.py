class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for seen in nums:
            if seen in hashSet:
                return True
            hashSet.add(seen)
        return False

