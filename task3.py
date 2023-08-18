
def searchInsert(target,l):
    left, right = 0 ,len(l) -1
    while left <= right:
        mid = (left + right )//2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

arr = list(map(int ,input().split()))

sorted_arr = []
for i in range(len(arr)):
    print(sorted_arr)
    pos = searchInsert(arr[-i],sorted_arr)
    sorted_arr = sorted_arr[0:pos] + [arr[-i]] + sorted_arr[pos::]

print(sorted_arr)
