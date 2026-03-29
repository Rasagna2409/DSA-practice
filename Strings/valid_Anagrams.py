s1 = input("enter string1 :")
s2 = input("enter string2 :")
if sorted(s1) == sorted(s2):
    print("given string are Anagrams",s1,s2)
else:
    print("Not Anagrams",s1,s2)