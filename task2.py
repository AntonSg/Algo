arr = list(map(int,input().split()))

c_pos = len(arr)
for i in range(len(arr)):
    # print(arr)
    max = arr[0]
    max_i = 0
    for i in range(c_pos):
        if arr[i] > max:
            max = arr[i]
            max_i = i
    c_pos -= 1
    arr[max_i],arr[c_pos] = arr[c_pos],arr[max_i]

print(arr)
