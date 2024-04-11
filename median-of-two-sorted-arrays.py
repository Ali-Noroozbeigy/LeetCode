class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        from math import inf
        nums1.append(inf)
        nums2.append(inf)

        even = False

        if m + n % 2 == 0:
            even = True
            median_index = (m+n-1) // 2
        else:
            median_index = (m+n) // 2

        i = 0
        p1 = 0
        p2 = 0
        while i < median_index:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
            i += 1

        if even:
            first = 0
            second = 0
            if nums1[p1] < nums2[p2]:
                first = nums1[p1]
                p1 += 1
            else:
                first = nums2[p2]
                p2 += 1
            if nums1[p1] < nums2[p2]:
                second = nums1[p1]
                p1 += 1
            else:
                second = nums2[p2]
                p2 += 1
            return (first + second) / 2
        else:
            if nums1[p1] < nums2[p2]:
                return float(nums1[p1])
            else:
                return float(nums2[p2])
