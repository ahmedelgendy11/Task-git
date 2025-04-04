
def multiplication_lists(num):
    lis = []
    for i in range(1,num + 1):
        lis2 = [j * i for j in range(1, i + 1)]
        lis.append(lis2)
    
    return lis

num=int(input("Enter a number: "))
result = multiplication_lists(number)
print(result)