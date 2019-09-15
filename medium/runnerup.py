# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen
n = int(input())
arr = list(str(input()).split(" "))
for i in range(0, len(arr)):
    for j in range(0, len(arr)) :
        if int(arr[i]) > int(arr[j]) :
            t = int(arr[i])
            arr[i] = int(arr[j])
            arr[j] = int(t)
arr2 = []
for i in arr :
    if i not in arr2 :
        arr2.append(int(i))
print (arr2[1])