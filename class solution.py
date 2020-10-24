def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []

    p1 = 0
    p2 = 0
    while p1 < m and p2 < n:  # 5 2 3  1 8 9
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1  #
    if p1 < m:
        for i in range(p1, m):
            nums1.append(nums1_copy[i])

    if p2 < n:
        # nums2[p1+p2:]=nums2[p2:]
        for i in range(p2, n):
            nums1.append(nums2[i])
    print(nums1)


merge([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3)
