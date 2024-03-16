# r=5
# c=5
# for i in range(1,r+1):
#     if i==1 or i==r:
#         for j in range(1,r+1):
#             print("X",end="")
        
#     else: 
#         for k in range(1,c+1):
#             if k==1 or k==c:
#                 print("X",end="")
#             else:
#                 print(" ",end="")
        
#     print()


# r = 5
# c = 5
# for i in range(1, r + 1):
#     if i == 1 or i == r:
#         for j in range(1, c + 1):
#             print("X", end=" ")
#     else:
#         print("X", end="")
#         for s in range(1, c):
#             print(" ", end="")
#         print("X", end="")
    # print()

r = 5
c = 5
for i in range(1, r + 1):
    for j in range(1, c + 1):
        if j == c or i == 1 or i == r:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
