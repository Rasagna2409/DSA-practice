s = input("enter string:")
s1 = set()
left = 0
max_len = 0
for right in range(len(s)):
    while s[right] in s1:
        s1.remove(s[left])
        left += 1
    s1.add(s[right])
    max_len = max(max_len, right-left+1)
print(max_len)