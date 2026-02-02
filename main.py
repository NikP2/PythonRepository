import os

def Min(ls):
    Min = float("inf")
    for c in ls:
        if c < Min:
            Min = c
    return Min

def Max(ls):
    Max = float("-inf")
    for c in ls:
        if c > Max:
            Max = c
    return Max

def Mean(ls):
    su = 0
    for c in ls:
        su += c
    return su / len(ls)

def Median(ls):
    sorted_ls = sorted(ls)
    middle = len(sorted_ls) // 2
    if len(sorted_ls) % 2 != 0:
        return sorted_ls[middle]
    else:
        return (sorted_ls[middle - 1] + sorted_ls[middle]) / 2


Dir = '/Users/nkt/Desktop/python/data'
frames = []
for file in os.listdir(Dir):
    frames.append(Dir + '/' + file)

with open("frames_out", "w") as file_out:
    for i in range(len(frames)):
        with open(frames[i], "r") as f:
            data = f.readlines()
            data_float = list(map(float, data))
            dic = {"Min":Min(data_float), "Max":Max(data_float), "Mean":Mean(data_float), "Median":Median(data_float)}
            file_out.write(frames[i] + str(dic.items()))
            file_out.write("\n")

# Task #2

# def validate_password(n):
#     alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     cif = '0123456789'
#     simb = '!@#$%^&*()_+-=[]{}|;:,.<>?`'
#     st = 0
#     za = 0
#     v1 = len(n) >= 8
#     v2 = False
#     v3 = False
#     v4 = False
#     v5 = False
#     for c1 in alf:
#         if c1 in n.upper():
#             v2 = True
#             break
#     for c2 in n:
#         if c2.isdigit():
#             v3 = True
#             break
#     for c3 in simb:
#         if c3 in n:
#             v4 = True
#             break
#     for c4 in n:
#         if c4 in alf:
#             za += 1
#         elif c4 in alf.lower():
#             st += 1
#     if za != 0 and st != 0:
#         v5 = True
#     return (v1 and v2 and v3 and v4 and v5, [v1, v2, v3, v4, v5])


# password = validate_password(input())

# while password[0] == False:
#     print(password)
#     password = validate_password(input("Не валидный пароль! Повтори попытку: "))
# print("Done!")
