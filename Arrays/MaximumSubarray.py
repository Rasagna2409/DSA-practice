arr = list(map(int, input("enter numbers:").split()))
max_arr = arr[0]
candidate = 0
for num in arr:
    candidate += num
    if candidate > max_arr:
        max_arr = candidate
    if candidate < 0:
        candidate = 0
print(max_arr)