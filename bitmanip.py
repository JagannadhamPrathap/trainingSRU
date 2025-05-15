# def xorwhole(n):
#     if n%4 == 1:
#         return 1
#     elif n%4 == 2:
#         return n+1
#     elif n%4 == 3:
#         return 0
#     else:
#         return n
# n = int(input())
# m = int(input())
# print(xorwhole(n-1)^xorwhole(m))
# n = int(input())
# if n&(n-1):
#     print("No")
# else:
#     print("Yes")
# nums = list(map(int,input().split()))
# i = 0
# while i<len(nums):
#     if nums[i] == nums[i+1]:
#         i+=2
#     else:
#         print(nums[i])
#         break
# else:
#     print(nums[-1])
# n = list(map(int,input().split()))
# c = 1
# m = 0
# for i in range(len(n)-1):
#     if n[i+1]-n[i] == 1:
#         c+=1
#     else:
#         c = 1
#     if c>m:
#         m = c
# print(m)
# s = input()
# k = []
# c = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c+=1
#     else:
#         k.append(s[i]+str(c))
#         c=1
# k.append(s[i]+str(c))
# print(*k)
dividend = 7
divisor = -3
c = 0
while dividend>divisor:
  dividend = dividend-divisor
  c+=1
print(-c if dividend<0 or divisor<0 else c)