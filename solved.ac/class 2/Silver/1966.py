# 1966번 프린터 큐
case = int(input())

for i in range(case):
    N, M = map(int, input().split())
    docs = [i for i in range(N)]
    important = list(map(int, input().split()))
    marker = docs[M]
    first = max(important)
    count = 0
    while True:
        first = max(important)
        if important[0] < first:
            important.append(important.pop(0))
            docs.append(docs.pop(0))
        else:
            if docs[0] == marker:
                count += 1
                break
            else:
                important.pop(0)
                docs.pop(0)
                count += 1
    print(count)
