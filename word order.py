from collections import Counter
n=int(input())
words=[]
for i in range(n):
    words.append(input())
count=Counter(words)
print(len(count))
print(*count.values())

