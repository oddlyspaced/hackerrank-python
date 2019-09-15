# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if int(year%4) == 0 :
        if int(year%100) == 0 :
            if int(year%400) == 0 :
                return True
            return False
        return True
    else :
        return False

year = int(input())
print(is_leap(year))