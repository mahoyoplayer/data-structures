def mergesort(arr):
    def merge(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        i1, i2 = 0, 0

        res = []
        while i1 < n1 and i2 < n2:
            if arr1[i1] <= arr2[i2]:
                res.append(arr1[i1])
                i1 += 1
            else:
                res.append(arr2[i2])
                i2 += 1
        for i in range(i1, n1):
            res.append(arr1[i])
        for i in range(i2, n2):
            res.append(arr2[i])
        return res
    
    # Base case
    if (n:=len(arr)) <= 1:
        return arr
    
    mid = n // 2
    l, r = mergesort(arr[:mid]), mergesort(arr[mid:])
    return merge(l, r)


test_arr = [9, 2, 4, 1]
print(mergesort(test_arr))