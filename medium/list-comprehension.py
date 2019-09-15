# https://www.hackerrank.com/challenges/list-comprehensions/problem
i = int(input())
j = int(input())
k = int(input())
n = int(input())
res = []
for a in range(0, i+1) :
    for b in range(0, j+1) :
        for c in range(0, k+1) :
            if int(a + b + c) != int(n) :
                r = []
                r.append(a)
                r.append(b)
                r.append(c)
                res.append(r)
print(res)