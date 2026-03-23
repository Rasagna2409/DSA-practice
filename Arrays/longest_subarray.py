def longsubstring():
    s = input("enter string:")
    n = len(s)
    left = 0
    max_len = 0
    charset = set()
    for right in range(n):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])
        max_len = max(max_len,right-left+1)
    print(max_len)
longsubstring()