# n=int(input("Enter the Row number: "))
# for i in range(n):
#     print(i+1,end=" ")
#     for k in range (n):
#         print(k+1,end=" ")
#     print("")
        
numbers = "12345"
for i in range(5):
    ones= ""
    for j in range(i):
        ones += "1"
    out = numbers[i:] + ones
    # print(numbers[i:])
    print(out)




# 12345

# 23451

# 34511

# 45111

# 51111