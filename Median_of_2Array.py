class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2!=0:
            return float(nums1[int(len(nums1)/2)])
        else:
            return float((nums1[int(len(nums1)/2-1)]+nums1[int(len(nums1)/2)])/2)
    