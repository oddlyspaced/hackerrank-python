# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# this problem requires us to find the element which is non repating in a list of input
grps = int(input())
inp = list((str(input()).split(" ")))
rooms = []
count = []

for i in inp :
    if int(i) not in rooms :
        rooms.append(int(i))
        count.append(int(1))
    else :
        count[rooms.index(int(i))] = count[rooms.index(int(i))] + 1

print(rooms[count.index(int(1))])