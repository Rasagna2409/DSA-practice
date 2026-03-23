arr = list(map(int,input("enter array numbers:").split()))
k = int(input("enter number for rotate:"))
n = len(arr)
k = k % n
arr[:] = arr[-k:] + arr[:-k]
print(arr)