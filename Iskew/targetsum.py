'''Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more

'''
n = int(input())
nums = list(map(int, input().split()))
t = int(input())

left = 0
right = len(nums) - 1

found = False

while left < right:
    summ = nums[left] + nums[right]
    if summ == t:
        found = True
        break
    elif summ < t:
        left += 1
    else:
        right -= 1

if found:
    print("Yes")
else:
    print("No")
