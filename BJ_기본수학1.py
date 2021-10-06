#1

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

if B >= C:
    print(-1)

else:
    print(int(A/(C-B)+1))


#2

n = int(input())

cnt = 1

cnt_six = 6

count = 1

while n > cnt:
    count += 1 # 몇 단계 인지 1, 1~7, 7~19...
    cnt += cnt_six # 증가량 -> 구간을 정해줌 1번째 구간에서 cnt_six 증가량을 더해서 구성 1층: 1, 2층 2~7 ,
    cnt_six += 6 # 증가량을 정해줌 6, 12, 18
print(count)


# 3

x = int(input())
num_list = []

num = 0  # 층을 위한 등차 수열
num_count = 0  # 몇층인지를 알 수 있게 해줌

while num_count < x:
    num += 1
    num_count += num

num_count -= num  # 이때 num_count = 15 이고, num이 5이므로, 5층에서 시작하려면 15 - 5빼고 10으로
# 시작하면된다

if num % 2 == 0:  # 만약 짝수층이라면
    i = x - num_count
    j = num - i + 1

else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i} / {j}")