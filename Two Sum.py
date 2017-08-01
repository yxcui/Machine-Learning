class Solution(object):
    def twoSum(self, nums, target):
        # type: (object, object) -> object
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        allindices = []
        for i in range(len(nums)):
            # The 'rest' is from 'target' minus each 'element' traversed from the list, and then judge whether the 'rest' is exist in list.
            rest = target - nums[i]

            if rest in nums:
                allindices.append((i, nums.index(rest)))

        indices = []
        for t in allindices:
            if t[0] != t[1]:
                indices.append(tuple(sorted(t)))
        return list(set(indices))

if __name__ == "__main__":
    s = Solution()
    indices = s.twoSum([0, 4, 3, 0], 0)    # Get a List containing several tuples(>=0)
    print indices
