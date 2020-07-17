class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        queue = []
        for key, value in freq.items():
            heapq.heappush(queue,(value,key))
            if len(queue)>k:
                heapq.heappop(queue)
        return [x for _,x in queue]
        