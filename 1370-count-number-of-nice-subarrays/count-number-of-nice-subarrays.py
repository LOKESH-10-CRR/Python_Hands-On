class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def edge(k):
            left = 0
            count = 0
            ans = 0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    count+=1
                while count>k:
                    if nums[left]%2==1:
                        count-=1
                    left+=1
                ans+=right-left+1
            return ans
        return edge(k)-edge(k-1)
        