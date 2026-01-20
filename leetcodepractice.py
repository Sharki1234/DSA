text = "pwwkew"
text_dict={}
total = 0
n = len(text)
for i in range(n):
    if text[i] in text_dict:
        total = 0
        n-=1
    else:
        text_dict[text[i]] = 0
        total+=1

print(total)
