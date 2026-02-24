s = "leetcode"
count = []
for i in range(len(s)):
    if s[i] not in s:
        print(i)
        break
   

    