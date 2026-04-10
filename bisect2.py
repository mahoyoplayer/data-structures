def bisect_right(arr: list, val: int):
    n = len(arr)
    l, r = 0, n
    while l < r:
        mid = (l+r)//2
        if arr[mid] <= val:
            l = mid+1
        else:
            r = mid
    return l



def bisect_left(arr: list, val: int):
    n = len(arr)
    l, r = 0, n
    while l < r:
        mid = (l+r)//2
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l

def binary_search(arr: list, val: int) -> bool:
    n = len(arr)
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < val:
            l = mid + 1
        elif arr[mid] > val:
            r = mid
        else:
            return mid
    return -1