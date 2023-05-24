    def majorityElement(nums: List[int]) -> int:

        """
        Passes only 42/45 test cases on Leetcode
        """
        n = len(nums) // 2
        for i in nums:
            if nums.count(i) > n:
                return i
