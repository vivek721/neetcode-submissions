class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        freqMap = {}
        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] +=  1
            else:
                freqMap[nums[i]]=1
        
        # Sort the items based on their frequency (val) in descending order
        sorted_items = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)
        
        res=[]
        # Take the first k elements from the sorted list
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
