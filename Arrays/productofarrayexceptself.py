arr = list(map(int, input("enter array:").split()))
n = len(arr)
res = [1]*n
for i in range(1,n):
    res[i] = res[i-1] * arr[i-1]
right = 1
for i in range(n-1,-1,-1):
    res[i] = res[i] * right
    right = right * arr[i]
print(res)