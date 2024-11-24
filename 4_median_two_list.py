class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1=sorted(nums1)
        if len(nums1) % 2 == 0:  
            mid1 = nums1[len(nums1) // 2 - 1]  
            mid2 = nums1[len(nums1) // 2]      
            return (float(mid1) + float(mid2)) / 2.0  
        else:  
            return nums1[len(nums1) // 2]  