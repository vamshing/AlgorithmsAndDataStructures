class BinarySearch(object):
    def Iterative(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int --index of the searched element if present ; else - 1
        """
        # Iterative Implementation of Binary Search
        left, right = 0, len(nums) - 1
        while((left <= right) and not found):
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # end condition right > left
        return -1

    def Recursive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int --index of the searched element if present ; else - 1
        """
        # Implements Binary Seach in Recursive fashion
        def Func(left, right):
            if left > right:
                return -1
            mid = (left + right) / 2
            if(nums[mid] == target):
                return mid
            else:
                if(nums[mid] > target):
                    return Func(left, mid - 1)
                else:
                    return Func(mid + 1, right)
        return Func(0, len(nums) - 1)
