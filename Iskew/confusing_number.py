'''def confusingNumberCount(N):
    rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    valid_digits = ['0', '1', '6', '8', '9']
    count = 0

    def is_confusing(num):
        rotated = ''
        for ch in reversed(str(num)):
            if ch not in rotate_map:
                return False
            rotated += rotate_map[ch]
        return rotated != str(num)

    def dfs(curr):
        nonlocal count
        if curr != '' and int(curr) <= N:
            if is_confusing(curr):
                count += 1
        for digit in valid_digits:
            if curr == '' and digit == '0':  
                continue
            new_num = curr + digit
            if int(new_num) > N:
                continue
            dfs(new_num)

    dfs('')
    return count
'''

n = int(input())
nums = list(range(1, n+1))

valid_digits = ['0', '1', '6', '8', '9']

for num in nums:
    string = str(num)
    flag=0
    count=0
    for ch in string:
        if ch not in valid_digits:
            flag=1
            break
    if flag==1:
        count+=1

print(count)

        
