# row = [False] * 4
# checked = [row] * 5
# print(checked)

# check = [[False] * 4] *5
# print(check)

# check = [[0]*3]
# print(check)

# for i in range(3, -1, -1):
#     print(i)

# res = [[0] * 4]
# def backtracking(tmp):
#     a = tmp[:]
#     for i in range(3, -1, -1):
#         a[i] = 1 - a[i]
#         if a not in res:
#             res.append(a)
#             print(a)
#             backtracking(a)
#         a[i] = 1 - a[i]

# backtracking(res[0])

# print([0] * 3)
# print(7^(7>>1))

# print(1234 % 100)

# test = [0] * 3
# test[1] = 2
# print(test)

# nums = [3,2,1,5,6,4]
# k = 2
# sorted_nums = [0] * len(nums)

# def divide(left, right):
#     if left == right:
#         return
#     mid = (left + right) // 2  
#     divide(left, mid)
#     divide(mid + 1, right)
#     conquer(left, mid, right)

# def conquer(left, mid, right):
#     tmp_l, tmp_r = left, mid + 1
#     for i in range(left, right + 1):
#         if tmp_l <= mid and tmp_r <= right:
#             if nums[tmp_l] >= nums[tmp_r]:
#                 sorted_nums[i] = nums[tmp_l]  
#                 tmp_l += 1
#             else: 
#                 sorted_nums[i] = nums[tmp_r]
#                 tmp_r += 1
#         else:
#             if tmp_l <= mid:
#                 sorted_nums[i] = nums[tmp_l]
#                 tmp_l += 1
#             elif tmp_r <= right:
#                 sorted_nums[i] = nums[tmp_r]
#                 tmp_r += 1
#     nums[left:right+1] = sorted_nums[left:right+1]


# divide(0, len(nums) - 1)
# print(sorted_nums)

# for i in range(5, 0, -1):
#     if i == 3:
#         break
# print(i)

# txt = "Hello my FRIENDS 2"
# x = txt.lower()
# print(x)

# print('A'.lower())

def valid_char(c):
    if '0' <= c <= '9' \
        or 'a' <= c <= 'z' \
        or 'A' <= c <= 'Z':
        print("ok")
    else:
        print("not ok")

valid_char('?')