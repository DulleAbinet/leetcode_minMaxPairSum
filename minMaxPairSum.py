class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nw_list = []
        left = 0
        right = len(nums)-1
        while left < right :
            nw_list.append(nums[left]+nums[right])
            left +=1
            right -=1
            
        return max(nw_list)
