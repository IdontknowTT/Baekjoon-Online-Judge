#상점에서 사야하는 물병의 최솟값을 출력한다
import sys
n,k = map(int, input().split())

count = 0

while bin(n).count('1') > k:
    n += 1
    count = count + 1

print(count)