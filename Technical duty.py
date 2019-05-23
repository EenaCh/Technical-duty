N, X, K = map(int, input().split())
t = [i for i in map(int, input().split())]
days_of_comments = sorted(t)
tN = days_of_comments[-1]

for i in t:
    count_dedline = 1
    while i + count_dedline * X < tN:
        if i + count_dedline not in days_of_comments:
            days_of_comments.append(i + count_dedline * X)
        count_dedline += 1

days_of_comments.sort()

i = 0
while True:
    if len(days_of_comments) == K:
        break
    if days_of_comments[i] + X not in days_of_comments:
        days_of_comments.append(days_of_comments[i] + X)
    i += 1

days_of_comments.sort()
print(days_of_comments[K - 1])
